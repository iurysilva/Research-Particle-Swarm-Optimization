import numpy as np


class Particle():
    def __init__(self):
        self.position = 0
        self.pbest = 0
        self.fitness = 0
        self.pbest_fitness = 0
        self.velocity = 0
        
    def generate_random_position(self, function):
        self.velocity = np.zeros(function.dimensions, dtype="float64")
        limits = np.copy(function.limits)
        self.position = np.array(np.random.uniform(limits[0], limits[1]+1, function.dimensions), dtype="float64")
    
    def update_pbest(self):
        if self.fitness < self.pbest_fitness:
            self.pbest = np.copy(self.position)
            self.pbest_fitness = np.copy(self.fitness)

    def find_fitness(self, function):
        return function.result(self.position)

