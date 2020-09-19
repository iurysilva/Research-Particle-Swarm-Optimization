import numpy as np


def update_particles_angles(swarm, algorithm_settings):
    new_angles = np.array([], dtype="float64")
    if algorithm_settings.function.dimensions == 2:
        for particle in swarm.particles:
            r = particle.position - particle.past_position
            angle = np.arctan2(r[1], r[0]) * 180 / np.pi
            if angle < 0:
                angle += 360
            new_angles = np.append(new_angles, angle)
        swarm.particles_angles = np.concatenate((swarm.particles_angles, new_angles))


def update_particle_position(swarm, algorithm_settings, particle, r1, r2, c1, c2):
    personal_component = (particle.pbest - particle.position) * (r1 * c1)
    global_component = (swarm.gbest - particle.position) * (r2 * c2)
    velocity = algorithm_settings.w * particle.velocity + (personal_component + global_component)
    particle.velocity = np.copy(velocity)
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


def do_one_iteration(swarm, algorithm_settings, iteration):
    for particle in swarm.particles:
        r1 = algorithm_settings.random_variable_method(algorithm_settings.function.dimensions)
        r2 = algorithm_settings.random_variable_method(algorithm_settings.function.dimensions)
        particle.past_position = np.copy(particle.position)
        update_particle_position(swarm, algorithm_settings, particle, r1, r2, algorithm_settings.c1, algorithm_settings.c2)
    update_particles_angles(swarm, algorithm_settings)
    swarm.particles = make_particles_stay_on_bounds(swarm, algorithm_settings, swarm.particles)
    swarm.update_particles_information(algorithm_settings.function)
    swarm.update_average_fitness(algorithm_settings.iterations, iteration)
    swarm.update_fitness_deviation(algorithm_settings.iterations, iteration)
