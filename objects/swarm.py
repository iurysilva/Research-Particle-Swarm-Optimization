import numpy as np
from . import Particle


def check_type(variable, iterations):
    if type(variable) == int:
        variable = np.zeros(iterations + 1)
    return variable


class Swarm():
    def __init__(self, particles_number=0):
        self.particles_number = particles_number
        self.particles = np.array([])
        self.gbest = 0
        self.gbest_fitness = 0
        self.particles_information = 0
        self.particles_angles = np.array([], dtype="float64")
        self.average_fitness = 0
        self.fitness_standart_deviation = 0
        self.function_minimum = 0

    def create_particles(self, function):
        for particle in range(0, self.particles_number):
            self.particles = np.append(self.particles, Particle())
            self.particles[particle].generate_random_position(function)
            if particle == 0:
                self.gbest = np.copy(self.particles[particle].position)
                self.gbest_fitness = self.particles[particle].fitness
            else:
                self.update_gbest(self.particles[particle])

    def update_gbest(self, particle):
        if particle.fitness < self.gbest_fitness:
            self.gbest = np.copy(particle.position)
            self.gbest_fitness = np.copy(particle.fitness)

    def update_particles_information(self, function):
        if type(self.particles_information) == int:
            self.particles_information = np.zeros(self.particles_number * (function.dimensions + 1), dtype="float64")
        for particle_number in range(self.particles_number):
            particle = self.particles[particle_number]
            self.particles_information[particle_number * 3] = particle.position[0]
            self.particles_information[particle_number * 3 + 1] = particle.position[1]
            self.particles_information[particle_number * 3 + 2] = particle.fitness
    
    def update_average_fitness(self, iterations, iteration):
        self.average_fitness = check_type(self.average_fitness, iterations)
        fitness = 0
        for i in self.particles:
            fitness = fitness+i.fitness
        self.average_fitness[iteration] = fitness/self.particles_number

    def update_fitness_deviation(self, iterations, iteration):
        self.fitness_standart_deviation = check_type(self.fitness_standart_deviation, iterations)
        deviation = 0
        average = self.average_fitness[-1]
        for i in self.particles:
            deviation = deviation+(i.fitness-average)**2
        self.fitness_standart_deviation[iteration] = np.sqrt(deviation/self.particles_number)
