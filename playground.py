import matplotlib.pyplot as plt
from objects import Swarm
from objects import AlgorithmSettings
from objects.benchmark_functions import *
from run_options import run_without_animation
from procedures.generate_random_variable_methods import *

function = Sphere()  # Sphere, Cross, Bukin6, Eggholder
particles_number = 50
random_variable_method = rotationally_variant  # rotationally_variant, rotationally_invariant
c1 = 2.05
c2 = 2.05
w = 0.5
iterations = 4000
animation_format = False  # False, '2D', 3D
precision = 1  # Pacing for the graphic building
animation_velocity = 20  # In millisecond's


algorithm_settings = AlgorithmSettings(iterations, particles_number, function, c1, c2, w, random_variable_method)
swarm = Swarm(particles_number)
swarm.create_particles(algorithm_settings.function)
swarm.update_particles_information(function)


if not animation_format:
    run_without_animation(algorithm_settings, swarm)
    
elif animation_format == '3D':
    ax = plt.axes(projection='3d')
    scat3D = ax.scatter3D(0, 0, 0)




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