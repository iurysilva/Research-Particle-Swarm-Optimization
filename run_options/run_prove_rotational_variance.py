from objects import Swarm
from objects import AlgorithmSettings
from run_options import run_without_animation
from procedures.generate_random_variable_methods import *


def prove_rotational_variance(iterations, particles_number, function, c1, c2, w, random_variable_method):
    executions_number = 20
    degree_average_list = np.array([], dtype='float64')
    for degree in range(360):
        print('doing %d degree' % degree)
        distance_list = np.array([], dtype='float64')
        for execution in range(executions_number):
            algorithm_settings = AlgorithmSettings(iterations, particles_number, function, c1, c2, w, random_variable_method)
            swarm = Swarm(particles_number)
            swarm.create_particles(algorithm_settings.function)
            algorithm_settings.function.rotation_number = degree
            run_without_animation(algorithm_settings, swarm)
            distance = swarm.gbest_fitness - algorithm_settings.function.function_minimum_fitness
            distance_list = np.append(distance_list, distance)
        degree_average_list = np.append(degree_average_list, np.sum(distance_list)/executions_number)
    return degree_average_list
