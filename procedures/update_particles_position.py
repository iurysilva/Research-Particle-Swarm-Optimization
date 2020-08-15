import random
import numpy as np


def update_information_list(swarm):
    #atualiza as posições x e y de cada particula na lista "particles_informations" no objeto Swarm
    for i in range(0,swarm.number_of_particles):
        particle= swarm.particles[i]
        swarm.particles_informations[i*3]= particle.position[0]
        swarm.particles_informations[i*3+1]= particle.position[1]
        swarm.particles_informations[i*3+2]= particle.fitness


def find_angle(past_position,new_position):
    #Coleta o angulo feito pelo movimento da particula em graus
    point= new_position-past_position
    if point[0]==0 and point[1]==0:
        return(-1)
    elif point[0]==0:
        if point[1]>0:
            return 90
        else:
            return 270
    else:
        coefficient= point[1]/point[0]
        if point[0]>0 and point[1]<0:
            return (np.degrees(np.arctan(coefficient))+360)
        elif point[0]<0 and point[1]<=0:
            return (np.degrees(np.arctan(coefficient))+180)
        elif point[0]<0 and point[1]>0:
            return (np.degrees(np.arctan(coefficient))+180)
        else:
            return (np.degrees(np.arctan(coefficient)))

def update_particles_position(swarm):
    # atualiza as velocidades e move as particulas
    # também atualiza o pbest e gbest a cada iteração
    global w, c1, c2, n, cont_angle, cont_iterations
    for i in range(0, swarm.number_of_particles):
        r1 = np.array([])
        r2 = np.array([])
        for j in range(swarm.dimensions):
            r1 = np.append(r1, random.random())
            r2 = np.append(r2, random.random())

        # r1= random.random()
        # r2= random.random()
        particle = swarm.particles[i]
        past_position = particle.position
        velocity = w * particle.velocity + (
                    (particle.pbest - particle.position) * (r1 * c1) + (swarm.gbest - particle.position) * (r2 * c2))
        particle.velocity = velocity
        particle.position = particle.position + velocity
        if swarm.dimensions == 2:
            swarm.angles[cont_angle] = find_angle(past_position, particle.position)
            cont_angle += 1
        for k in range(swarm.dimensions):
            # trazendo a particula para a borda, caso ele ultrapasse os limites
            if particle.position[k] < swarm.limits[0]:
                particle.position[k] = swarm.limits[0]
            elif particle.position[k] > swarm.limits[1]:
                particle.position[k] = swarm.limits[1]
        particle.fitness = particle.find_fitness(function)
        particle.update_pbest()
        swarm.update_gbest(particle)
    swarm.average_fitness[cont_iterations] = swarm.find_average()
    swarm.fitness_standart_deviation[cont_iterations] = swarm.find_deviation()
    cont_iterations += 1