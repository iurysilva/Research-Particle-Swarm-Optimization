import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from procedures import do_one_iteration
from procedures import make_histogram
import numpy as np

ax1 = plt.axes(projection='3d')
scat3d = ax1.scatter3D(0, 0, 0)
anim = 0
algorithm_settings = 0
swarm = 0


def plot_3d_graphic():
    global ax1, algorithm_settings
    function = algorithm_settings.function
    precision = algorithm_settings.function.precision
    plt.title('iterations left: %d' % algorithm_settings.iterations)
    plt.xlim(function.limits[0]-1, function.limits[1]+1)
    plt.ylim(function.limits[0]-1, function.limits[1]+1)
    x_list = np.arange(function.limits[0]-1, function.limits[1]+1.5, precision)
    y_list = np.arange(function.limits[0]-1, function.limits[1]+1.5, precision)
    new_x, new_y = np.meshgrid(x_list, y_list)
    z = function.result(np.array([new_x, new_y]))
    ax1.contour3D(new_x, new_y, z, 50)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')
    ax1.view_init(50, 270)


def animation3d(frame):
    global ax1, scat3d, anim, algorithm_settings, swarm
    scat3d.remove()
    aux = swarm.particles_information
    scat3d = ax1.scatter3D(aux[::3], aux[1::3], aux[2::3], c=['k'])
    do_one_iteration(swarm, algorithm_settings, algorithm_settings.iteration)
    algorithm_settings.iterations -= 1
    algorithm_settings.iteration += 1
    plt.title('iterations left: %d' % (algorithm_settings.iterations+1))
    if algorithm_settings.iterations == -1:
        anim.event_source.stop()
        make_histogram(algorithm_settings, swarm)


def run_animation_3d(algorithm_settings2, swarm2, animation_velocity):
    global anim, algorithm_settings, swarm, precision
    algorithm_settings = algorithm_settings2
    swarm = swarm2
    print("Initializing with 3D animation")
    anim = FuncAnimation(plt.gcf(), animation3d, interval=animation_velocity, repeat=False, init_func=plot_3d_graphic)
    plt.show()
