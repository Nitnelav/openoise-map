import jnius_config
import os

if not jnius_config.vm_running:
    jnius_config.add_options('-Xmx4096m')
    jnius_config.set_classpath(os.path.join(os.path.dirname(__file__), '..', 'noisemodelling-libs/*'))

from jnius import autoclass

# # Imports
RoadSourceParametersCnossos = autoclass('org.noise_planet.noisemodelling.emission.RoadSourceParametersCnossos')
EvaluateRoadSourceCnossos = autoclass('org.noise_planet.noisemodelling.emission.EvaluateRoadSourceCnossos')
CnossosPropagationData = autoclass('org.noise_planet.noisemodelling.pathfinder.CnossosPropagationData')
RunnerMain = autoclass('org.noisemodelling.runner.Main')
LoggerFactory = autoclass('org.slf4j.LoggerFactory')
PropagationDataBuilder = autoclass('org.noise_planet.noisemodelling.pathfinder.PropagationDataBuilder')
ComputeCnossosRays = autoclass('org.noise_planet.noisemodelling.pathfinder.ComputeCnossosRays')
IComputeRaysOut = autoclass('org.noise_planet.noisemodelling.pathfinder.IComputeRaysOut')
ProfileBuilder = autoclass('org.noise_planet.noisemodelling.pathfinder.ProfileBuilder')
ProfilerThread = autoclass('org.noise_planet.noisemodelling.pathfinder.utils.ProfilerThread')
ComputeRaysOutAttenuation = autoclass('org.noise_planet.noisemodelling.propagation.ComputeRaysOutAttenuation')
PropagationProcessPathData = autoclass('org.noise_planet.noisemodelling.propagation.PropagationProcessPathData')
Coordinate = autoclass('org.locationtech.jts.geom.Coordinate')
Array = autoclass('java.lang.reflect.Array')

