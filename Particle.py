import numpy as np
import random
from Swarm import Swarm
class Particle():
    def __init__(self,limits,swarm):
        self.position= self.define_position(limits,swarm)
        self.pbest= self.position
        self.fitness= swarm.find_fitness(self.position)
        self.pbest_fitness= self.fitness
        self.velocity= np.zeros(swarm.dimensions)
        
    def define_position(self,limits,swarm): #Irá gerar as particulas em uma posição aleatória entre os limites
        for i in range(0,swarm.dimensions):
            if i==0:
                self.position= np.array([random.uniform(swarm.limits[0],swarm.limits[1])],dtype="float64")
            else:
                self.position= np.insert(self.position,i,random.uniform(swarm.limits[0],swarm.limits[1]))
        return self.position
    
    def update_pbest(self): #atualiza o pbest
        if self.fitness<self.pbest_fitness:
            self.pbest= self.position
            self.pbest_fitness= self.fitness

    
