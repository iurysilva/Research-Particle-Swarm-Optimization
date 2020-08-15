import numpy as np
from . import Particle


class Swarm():
    def __init__(self, particles=np.array([]), particles_number=0):
        self.particles_number = particles_number
        self.particles = particles
        self.gbest = 0
        self.gbest_fitness = []
        self.particles_informations= 0
        self.particles_angles = np.array([], dtype="float64")
        self.average_fitness= 0
        self.fitness_standart_deviation=0
        self.function_minimum= 0

    def create_particles(swarm):  # cria as particulas
        for i in range(0, swarm.number_of_particles):
            if i == 0:
                swarm.particles = np.array([Particle(swarm.limits, swarm)])
                swarm.gbest = swarm.particles[i].position
                swarm.gbest_fitness = swarm.particles[i].fitness
            else:
                swarm.particles = np.insert(swarm.particles, i, Particle(swarm.limits, swarm))
                swarm.update_gbest(swarm.particles[i])

    def update_gbest(self,particle):
        if particle.fitness<self.gbest_fitness:
            self.gbest= particle.position
            self.gbest_fitness= particle.fitness
    
    def find_average(self): #calcula média do fitness na iteração atual
        fitness= 0
        for i in self.particles:
            fitness= fitness+i.fitness
        return fitness/self.particles_number

    def find_deviation(self): #calcula desvio padrão do fitness na iteração atual
        deviation= 0
        average= self.average_fitness[-1]
        for i in self.particles:
            deviation= deviation+(i.fitness-average)**2
        return np.sqrt(deviation/self.particles_number)
