from procedures import do_one_iteration
from procedures import make_histogram


def run_without_animation(algorithm_settings, swarm):
    for iteration in range(algorithm_settings.iterations):
        do_one_iteration(swarm, algorithm_settings, iteration)
    make_histogram(algorithm_settings, swarm)
