def create_particles(swarm): #cria as particulas
    for i in range(0,swarm.number_of_particles):
        if i==0:
            swarm.particles= np.array([Particle(swarm.limits,swarm)])
            swarm.gbest= swarm.particles[i].position
            swarm.gbest_fitness= swarm.particles[i].fitness
        else:
            swarm.particles= np.insert(swarm.particles,i,Particle(swarm.limits,swarm))
            swarm.update_gbest(swarm.particles[i])
