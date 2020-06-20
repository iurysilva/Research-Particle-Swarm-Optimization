import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Functions
class Swarm():
    def __init__(self):
        self.number_of_particles= 10
        self.particles= []
        self.dimensions= 2 #sem contar com a dimensão adicional do fitness
        self.limits= np.array([-10,10],dtype="int64")
        self.gbest= []
        self.gbest_fitness= []
        self.particles_informations= 0
        self.angles= 0
        self.function= Functions.Cross
        self.average_fitness= 0
        self.fitness_standart_deviation=0
        self.function_minimum= 0
        
    def update_gbest(self,particle):
        if particle.fitness<self.gbest_fitness:
            self.gbest= particle.position
            self.gbest_fitness= particle.fitness
    
    def find_average(self): #calcula média do fitness na iteração atual
        fitness= 0
        for i in self.particles:
            fitness= fitness+i.fitness
        return fitness/self.number_of_particles

    def find_deviation(self): #calcula desvio padrão do fitness na iteração atual
        deviation= 0
        average= self.average_fitness[-1]
        for i in self.particles:
            deviation= deviation+(i.fitness-average)**2
        return np.sqrt(deviation/self.number_of_particles)
        
            
    def find_fitness(self,x): #Valor x deverá ser um array com os valores X e Y.
        return self.function(x,self)
    
