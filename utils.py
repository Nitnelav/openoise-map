from genericpath import isfile
import sys, site, os
import subprocess, shutil

def ensure_pyjnius():
    if site.USER_SITE not in sys.path:
        sys.path.append(site.USER_SITE)
    try:
        import jnius_config
        return True
    except:
        print("Dependency pyjnius not found, trying to install it...")
        print("Running command : " + shutil.which('python3') + ' -m pip install pyjnius --user')
        check = subprocess.run(
            shutil.which('python3') + ' -m pip install pyjnius --user',
            check=False,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        if (check.returncode != 0):
            print("Pyjnius installation failed, please report this error to the plugin author")
            return False
        print("Running command : " + shutil.which('python3') + ' -c "import sys; print(\';\'.join(sys.path))"')
        check = subprocess.run(
            shutil.which('python3') + ' -c "import sys; print(\';\'.join(sys.path))"',
            check=False,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        if (check.returncode != 0):
            print("Pyjnius installation failed, please report this error to the plugin author")
            return False

        print("Adding pyjnius to the QGIS embedded python sys.path")
        for p in check.stdout.strip().split(";"):
            if p not in sys.path:
                sys.path.append(p)
        try:
            import jnius_config
            print("Pyjnius sucessfully installed")
            return True
        except:
            print("Pyjnius installation failed, please report this error to the plugin author")
            return False

        return True

def ensure_jdk():
    if sys.platform == 'win32':
        jdk_path = os.path.join(os.path.dirname(__file__), "jdk-11.0.2")
        jdk_zip_path = os.path.join(os.path.dirname(__file__), "jdk-11.0.2.zip")

        if not os.path.isdir(jdk_path) and os.path.isfile(jdk_zip_path):
            import zipfile
            print("java jdk zip file found, extracting archive...")
            with zipfile.ZipFile(jdk_zip_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(jdk_path))
            print("extracting java jdk zip file done.")

        if os.path.isdir(jdk_path):
            os.environ["JAVA_HOME"] = jdk_path
            os.environ["PATH"] = os.environ["PATH"] + ";" + jdk_path
            os.environ["PATH"] = os.environ["PATH"] + ";" + os.path.join(jdk_path, "bin")
            os.environ["PATH"] = os.environ["PATH"] + ";" + os.path.join(jdk_path, "bin", "server")
            return True

    return False

def ensure_noisemodelling():
    nm_path = os.path.join(os.path.dirname(__file__), "noisemodelling-libs")
    nm_zip_path = os.path.join(os.path.dirname(__file__), "noisemodelling-libs.zip")

    if not os.path.isdir(nm_path) and os.path.isfile(nm_zip_path):
        import zipfile
        print("noisemodelling zip file found, extracting archive...")
        with zipfile.ZipFile(nm_zip_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(nm_path))
        print("extracting noisemodelling zip file done.")

    if os.path.isdir(nm_path):
        return True

    return False

def ensure_java_env(jdk_path):