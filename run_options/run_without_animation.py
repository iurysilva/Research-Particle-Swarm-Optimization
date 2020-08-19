from procedures import do_one_iteration
from procedures import do_one_iteration_fast


def run_without_animation(algorithm_settings, swarm, rotation_variance=False):
    for iteration in range(algorithm_settings.iterations):
        if not rotation_variance:
            do_one_iteration(swarm, algorithm_settings, iteration)
        else:
            do_one_iteration_fast(swarm, algorithm_settings)
