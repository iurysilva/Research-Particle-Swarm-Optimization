import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from objects.particle import Particle
from objects.swarm import Swarm
from objects.benchmark_functions import *

swarm= Swarm() #inicializando objeto Swam

'''--------------------Variáveis globais para execução personalizada--------------------'''
#funções disponíveis:
#Ackley,Quadratic,Cross,Easom,Beale,Booth,Bukin6,Eggholder,Schaffer2,Rastrigin
swarm.function= Tang
swarm.number_of_particles= 50
swarm.dimensions= 2  #Só há funções para 2 dimensões disponíveis
animation_format= '3D'
c1 = 2.05
c2 = 2.05
w= 0.5
iterations=200
precision= 1 #quanto menor (abaixo de 1), maior a qualidade do gráfico
animation_velocity= 1 #intervalo entre iterações em milissegundos



if animation_format=='2D':
    scat2D= plt.scatter(0,0)
    
elif animation_format=='3D':
    ax= plt.axes(projection= '3d')
    scat3D= ax.scatter3D(0,0,0)




"""-------------------Funções para o desenho e animação do gráfico em Matplotlib--------------------"""
'''
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
'''

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
