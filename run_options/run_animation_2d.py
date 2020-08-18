import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from procedures import do_one_iteration
from procedures import make_histogram
import numpy as np


scat2d = 0
anim = 0
algorithm_settings = 0
swarm = 0


def animation2d(frame):
    global scat2d, algorithm_settings, swarm
    limits = algorithm_settings.function.limits
    plt.xlim(limits[0]-1, limits[1]+1)
    plt.ylim(limits[0]-1, limits[1]+1)
    scat2d.remove()
    positions = np.copy(swarm.particles_information)
    scat2d = plt.scatter(positions[::3], positions[1::3], c=['k'])
    do_one_iteration(swarm, algorithm_settings, algorithm_settings.iteration)
    algorithm_settings.iteration += 1
    algorithm_settings.iterations -= 1
    plt.title('iterations left: %d' % (algorithm_settings.iterations+1))
    if algorithm_settings.iterations == -1:
        anim.event_source.stop()
        make_histogram(algorithm_settings, swarm)


def run_animation_2d(algorithm_settings2, swarm2, animation_velocity):
    global anim, algorithm_settings, swarm, scat2d
    algorithm_settings = algorithm_settings2
    swarm = swarm2
    scat2d = plt.scatter(0, 0)
    print("Initializing with 2D animation")
    anim = FuncAnimation(plt.gcf(), animation2d, interval=animation_velocity, repeat=False)
    plt.show()
