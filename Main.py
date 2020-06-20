import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from Particle import Particle
from Swarm import Swarm
from Functions import *

swarm= Swarm() #inicializando objeto Swam

'''--------------------Variáveis globais para execução personalizada--------------------'''
#funções disponíveis:
#Ackley,Quadratic,Cross,Easom,Beale,Booth,Bukin6,Eggholder,Schaffer2,Rastrigin
swarm.function= Cross
swarm.number_of_particles= 50
swarm.dimensions= 2  #Só há funções para 2 dimensões disponíveis
animation_format= '2D'
c1 = 2.05
c2 = 2.05
w= 0.5
iterations=200
precision= 20 #quanto menor (abaixo de 1), maior a qualidade do gráfico
animation_velocity= 1 #intervalo entre iterações em milissegundos



if animation_format=='2D':
    scat2D= plt.scatter(0,0)
    
elif animation_format=='3D':
    ax= plt.axes(projection= '3d')
    scat3D= ax.scatter3D(0,0,0)




'''--------------------Funções para o PSO-------------------- '''
def create_particles(swarm): #cria as particulas
    for i in range(0,swarm.number_of_particles):
        if i==0:
            swarm.particles= np.array([Particle(swarm.limits,swarm)])
            swarm.gbest= swarm.particles[i].position
            swarm.gbest_fitness= swarm.particles[i].fitness
        else:
            swarm.particles= np.insert(swarm.particles,i,Particle(swarm.limits,swarm))
            swarm.update_gbest(swarm.particles[i])



def update_position(swarm):
    #atualiza as velocidades e move as particulas
    #também atualiza o pbest e gbest a cada iteração
    global w,c1,c2,n,cont_angle,cont_iterations
    for i in range(0,swarm.number_of_particles):
        r1=np.array([])
        r2=np.array([])
        for j in range(swarm.dimensions):
            
            r1= np.append(r1,random.random())
            r2= np.append(r2,random.random())
            
        #r1= random.random()
        #r2= random.random()
        particle=swarm.particles[i]
        past_position= particle.position
        velocity= w*particle.velocity+((particle.pbest-particle.position)*(r1*c1) + (swarm.gbest-particle.position)*(r2*c2))
        particle.velocity= velocity
        particle.position= particle.position+velocity
        if swarm.dimensions==2:
            swarm.angles[cont_angle]= find_angle(past_position,particle.position)
            cont_angle+=1
        for k in range(swarm.dimensions):
            #trazendo a particula para a borda, caso ele ultrapasse os limites
            if particle.position[k]<swarm.limits[0]:
                particle.position[k]=swarm.limits[0]
            elif particle.position[k]>swarm.limits[1]:
                particle.position[k]= swarm.limits[1]
        particle.fitness= swarm.find_fitness(particle.position)
        particle.update_pbest()
        swarm.update_gbest(particle)
    swarm.average_fitness[cont_iterations]= swarm.find_average()
    swarm.fitness_standart_deviation[cont_iterations]= swarm.find_deviation()
    cont_iterations+=1


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

"""-------------------Funções para o desenho e animação do gráfico em Matplotlib--------------------"""
    
def plot_grafic():
    global ax,precision,iterations
    #desenha o gráfico apenas para 3 dimensões (contando com o fitness)
    plt.title('iterações restantes: %d'%iterations)
    plt.xlim(swarm.limits[0]-1,swarm.limits[1]+1)
    plt.ylim(swarm.limits[0]-1,swarm.limits[1]+1)
    x_list = np.arange(swarm.limits[0]-1,swarm.limits[1]+1.5,precision)
    y_list = np.arange(swarm.limits[0]-1,swarm.limits[1]+1.5,precision)
    new_X, new_Y=np.meshgrid(x_list,y_list)
    z= swarm.find_fitness(np.array([(new_X),(new_Y)]))
    ax.contour3D(new_X, new_Y, z,100)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.view_init(50, 270)
    

def histogram():
    global n
    plt.clf()
    plt.title('Gbest final: (X= %f, Y= %f)\n\n Minimo da função: (X= %f, Y= %f)'%(swarm.gbest[0],swarm.gbest[1],swarm.function_minimum[0],swarm.function_minimum[1]))
    plt.xticks(np.arange(0,361,30))
    plt.hist(swarm.angles,100)
    

def animation3D(frame):
    global scat3D,iterations
    #animação apenas para funções com 3 dimensões (contando com o fitness
    scat3D.remove()
    aux=swarm.particles_informations
    scat3D = ax.scatter3D(aux[::3],aux[1::3],aux[2::3],c =  ['k'])
    update_position(swarm)
    update_information_list()
    iterations-=1
    plt.title('iterações restantes: %d'%(iterations+1))
    if iterations==-1:
        anim.event_source.stop()
        histogram()



def animation2D(frame):
    global scat2D,iterations
    #animação para verificar o bias
    plt.xlim(swarm.limits[0]-1,swarm.limits[1]+1)
    plt.ylim(swarm.limits[0]-1,swarm.limits[1]+1)
    scat2D.remove()
    aux=swarm.particles_informations
    scat2D = plt.scatter(aux[::3],aux[1::3],c =  ['k'])
    update_position(swarm)
    update_information_list()
    iterations-=1
    plt.title('iterações restantes: %d'%(iterations+1))
    if iterations==-1:
        anim.event_source.stop()
        histogram()



def update_information_list():
    #atualiza as posições x e y de cada particula na lista "particles_informations" no objeto Swarm
    for i in range(0,swarm.number_of_particles):
        particle= swarm.particles[i]
        swarm.particles_informations[i*3]= particle.position[0]
        swarm.particles_informations[i*3+1]= particle.position[1]
        swarm.particles_informations[i*3+2]= particle.fitness



"""-------------------Execução do código--------------------"""
cont_angle=0
cont_iterations=0
swarm.function(np.array([1,2]),swarm)
create_particles(swarm) #inicializando um array com todas as particulas
swarm.particles_informations= np.zeros(swarm.number_of_particles*3,dtype="float64")
swarm.angles= np.zeros(swarm.number_of_particles*(iterations+1),dtype="float64")
swarm.average_fitness= np.zeros(iterations+1)
swarm.fitness_standart_deviation= np.zeros(iterations+1)
if swarm.dimensions==2: #animação apenas será feita com funções de 2 dimensões
    update_information_list() #atualizando as posições x e y de cada particula na lista "particles_informations (para ser utilizada nas funções de plot)
    if animation_format=='3D':
        anim= FuncAnimation(plt.gcf(),animation3D,interval=animation_velocity,repeat=False,init_func= plot_grafic) #inicia animação
    elif animation_format=='2D':
        anim= FuncAnimation(plt.gcf(),animation2D,interval=animation_velocity,repeat=False) #inicia animação
    plt.show()
else:
    '''
    for i in range(0,iterations):
        update_position(swarm)
    print('Posição do gbest na ordem X,Y,Z...')
    for i in range(swarm.dimensions):
        print ('{0:.10f}'.format(swarm.gbest[i]))
    '''
