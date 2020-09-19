from objects import Swarm
from run_options import run_without_animation
from procedures.generate_random_variable_methods import *


def prove_rotational_variance(algorithm_settings, executions_number, degrees):
    degree_average_list = np.array([], dtype='float64')
    for degree in range(degrees):
        algorithm_settings.function.rotation_number = degree
        print('doing %d degree' % degree)
        distance_list = np.array([], dtype='float64')
        for execution in range(executions_number):
            swarm = Swarm(algorithm_settings.particles_number)
            swarm.create_particles(algorithm_settings.function)
            run_without_animation(algorithm_settings, swarm, True)
            distance = swarm.gbest_fitness - algorithm_settings.function.function_minimum_fitness
            distance_list = np.append(distance_list, distance)
        degree_average_list = np.append(degree_average_list, np.sum(distance_list)/executions_number)
    return degree_average_list
