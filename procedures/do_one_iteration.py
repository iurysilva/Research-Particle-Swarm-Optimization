from procedures.generate_random_variable_methods import *


def balance_components(velocity):
    vector = np.array([1, -1])
    n = np.random.randint(0, 2)
    if np.random.uniform(0, 1) < 0.37:
        if np.abs(velocity[0]) < np.abs(velocity[1])*0.17:
            velocity[0] += velocity[1] * np.random.uniform(0, 2) * vector[n]
        elif np.abs(velocity[1]) < np.abs(velocity[0]) * 0.17:
            velocity[1] += velocity[0] * np.random.uniform(0, 2) * vector[n]
    return velocity


def balance_components2(velocity, dimensions):
    vector = np.array([1, -1])
    media = (np.sum(velocity)) / dimensions
    for i in range(0, dimensions):
        if np.abs(velocity[i]) < np.abs(media)*0.5 and np.random.uniform(0, 1) < 0.5:
            signal = np.random.randint(0, 2)
            velocity += np.abs(media) * np.random.uniform(0, 1) * vector[signal]
    return velocity


def update_particles_angles(swarm):
    new_angles = np.array([], dtype="float64")
    for particle in swarm.particles:
        r = particle.position - particle.past_position
        angle = np.arctan2(r[1], r[0]) * 180 / np.pi
        if angle < 0:
            angle += 360
        new_angles = np.append(new_angles, angle)
    swarm.particles_angles = np.concatenate((swarm.particles_angles, new_angles))


def update_particle_position(swarm, algorithm_settings, particle, r1, r2):
    dimensions = algorithm_settings.function.dimensions
    c1 = algorithm_settings.c1
    c2 = algorithm_settings.c2
    personal_component = (particle.pbest - particle.position) * (r1 * c1)
    global_component = (swarm.gbest - particle.position) * (r2 * c2)
    velocity = algorithm_settings.w * particle.velocity + (personal_component + global_component)
    if algorithm_settings.modify_velocity:
        velocity = balance_components2(velocity, dimensions)
    particle.velocity = np.copy(velocity)
    particle.position = particle.position + velocity
    particle.position += 0.00000000000000001


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
        update_particle_position(swarm, algorithm_settings, particle, r1, r2)
    update_particles_angles(swarm)
    swarm.particles = make_particles_stay_on_bounds(swarm, algorithm_settings, swarm.particles)
    swarm.update_particles_information(algorithm_settings.function)
    swarm.update_average_fitness(algorithm_settings.iterations, iteration)
    swarm.update_fitness_deviation(algorithm_settings.iterations, iteration)
