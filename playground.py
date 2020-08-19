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
function = Eggholder()  # Sphere(), Cross(), Bukin6(), Eggholder(), Booth()
particles_number = 10
random_variable_method = rotationally_invariant  # rotationally_variant, rotationally_invariant
c1 = 2.05
c2 = 2.05
w = 0.5
iterations = 50
executions_number = 20  # Used in rotational variance run_purpose
degrees_to_rotate = 360  # Used in rotational variance run_purpose
animation_format = '3D'  # False, '2D', '3D'
animation_velocity = 20  # In millisecond's


algorithm_settings = AlgorithmSettings(iterations, particles_number, function, c1, c2, w, random_variable_method)
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
    #plt.ylim(0, 0.00006)
    plt.plot(np.arange(0, degrees_to_rotate), result)
    plt.show()
else:
    print('run_purpose not correctly defined')
