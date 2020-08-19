import numpy as np


def update_particle_position(swarm, algorithm_settings, particle, r1, r2, c1, c2):
    personal_component = (particle.pbest - particle.position) * (r1 * c1)
    global_component = (swarm.gbest - particle.position) * (r2 * c2)
    velocity = algorithm_settings.w * particle.velocity + (personal_component + global_component)
    particle.velocity = velocity
    particle.position = particle.position + velocity


def make_particles_stay_on_bounds(swarm, algorithm_settings, particles):
    inferior_limit = algorithm_settings.function.limits[0]
    superior_limit = algorithm_settings.function.limits[1]
    for particle in particles:
        for dimension in range(algorithm_settings.function.dimensions):
            if particle.position[dimension] < inferior_limit:
                particle.position[dimension] = inferior_limit
            elif particle.position[dimension] > superior_limit:
                particle.position[dimension] = superior_limit
        particle.fitness = particle.find_fitness(algorithm_settings.function)
        particle.update_pbest()
        swarm.update_gbest(particle)
    return particles


def do_one_iteration_fast(swarm, algorithm_settings):
    for particle in swarm.particles:
        r1 = algorithm_settings.random_variable_method(algorithm_settings.function.dimensions)
        r2 = algorithm_settings.random_variable_method(algorithm_settings.function.dimensions)
        particle.past_position = np.copy(particle.position)
        update_particle_position(swarm, algorithm_settings, particle, r1, r2, algorithm_settings.c1, algorithm_settings.c2)
    swarm.particles = make_particles_stay_on_bounds(swarm, algorithm_settings, swarm.particles)

