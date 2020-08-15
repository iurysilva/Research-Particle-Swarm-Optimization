import numpy as np
import matplotlib.pyplot as plt


def make_histogram(algorithm_settings, swarm):
    print("Creating a histogram with movement angles")
    f_minimum = algorithm_settings.function.function_minimum
    best = swarm.gbest
    plt.clf()
    plt.title('Best position found: (X= %f, Y= %f)\n\n Function minimum: (X= %f, Y= %f)' % (best[0], best[1], f_minimum[0], f_minimum[1]))
    plt.xticks(np.arange(0, 361, 45))
    plt.hist(swarm.particles_angles, 100)
    plt.show()
