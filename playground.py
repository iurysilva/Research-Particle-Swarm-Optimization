from objects import Swarm
from objects import AlgorithmSettings
from objects.benchmark_functions import *
from run_options import run_without_animation
from run_options import run_animation_2d
from run_options import run_animation_3d
from procedures.generate_random_variable_methods import *

function = Eggholder()  # Sphere, Cross, Bukin6, Eggholder
particles_number = 50
random_variable_method = rotationally_variant  # rotationally_variant, rotationally_invariant
c1 = 2.05
c2 = 2.05
w = 0.5
iterations = 200
animation_format = '3D'  # False, '2D', 3D
animation_velocity = 20  # In millisecond's


algorithm_settings = AlgorithmSettings(iterations, particles_number, function, c1, c2, w, random_variable_method)
swarm = Swarm(particles_number)
swarm.create_particles(algorithm_settings.function)
swarm.update_particles_information(function)

    
if animation_format == '2D':
    run_animation_2d(algorithm_settings, swarm, animation_velocity)
elif animation_format == '3D':
    run_animation_3d(algorithm_settings, swarm, animation_velocity)
else:
    run_without_animation(algorithm_settings, swarm)
