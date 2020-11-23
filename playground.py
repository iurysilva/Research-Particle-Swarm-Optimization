from objects import Swarm
from objects import AlgorithmSettings
from objects.benchmark_functions import *
import matplotlib.pyplot as plt
from run_options import run_without_animation
from run_options import run_animation_2d
from run_options import run_animation_3d
from run_options import prove_rotational_variance
from procedures.generate_random_variable_methods import *
from procedures.make_histogram import make_histogram

run_purpose = 'bias'   # 'bias', 'rotational_variance'
function = Sphere()  # Sphere(), Cross(), Bukin6(), Eggholder(), Booth(), Easom(), Schaffer2()
function.dimensions = 2
function.rotation_number = 0
particles_number = 50
modify_velocity = False
random_variable_method = rotationally_variant  # rotationally_variant, rotationally_invariant
c1 = 2.05
c2 = 2.05
w = 0.5
iterations = 1000
executions_number = 20  # Used in rotational variance run_purpose
degrees_to_rotate = 360  # Used in rotational variance run_purpose
animation_format = '2'  # False, '2D', '3D'
animation_velocity = 20  # In millisecond's


if modify_velocity:
    c1 = 1.7
    c2 = 1.7

algorithm_settings = AlgorithmSettings(iterations, particles_number, function, c1, c2, w, random_variable_method, modify_velocity)
swarm = Swarm(particles_number)
swarm.create_particles(algorithm_settings.function)
swarm.update_particles_information(function)

if run_purpose == 'bias':
    if animation_format == '2D':
        run_animation_2d(algorithm_settings, swarm, animation_velocity)
    elif animation_format == '3D':
        run_animation_3d(algorithm_settings, swarm, animation_velocity)
        print(swarm.gbest_fitness)
    else:
        run_without_animation(algorithm_settings, swarm)
        make_histogram(algorithm_settings, swarm)
elif run_purpose == 'rotational_variance':
    result = prove_rotational_variance(algorithm_settings, executions_number, degrees_to_rotate)
    #plt.ylim(0, 800000)
    plt.plot(np.arange(0, degrees_to_rotate), result)
    plt.show()
else:
    print('run_purpose not correctly defined')
