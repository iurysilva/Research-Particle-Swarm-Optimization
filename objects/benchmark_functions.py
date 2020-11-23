import numpy as np


def rotate_x(x, y, theta):
    return x * np.cos(theta) - y * np.sin(theta)


def rotate_y(x, y, theta):
    return y * np.cos(theta) + x * np.sin(theta)


class Bukin6:
    def __init__(self):
        self.limits = np.array([-15, 3], dtype="int64")
        self.function_minimum = np.array([-10, 1])
        self.function_minimum_fitness = 0
        self.dimensions = 2
        self.precision = 0.5
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        return 100 * (np.sqrt(np.absolute(x1 - 0.01 * x0 ** 2))) + (0.01 * np.absolute(x0 + 10))


class Eggholder:
    def __init__(self):
        self.limits = np.array([-512, 512], dtype="int64")
        self.function_minimum = np.array([512, 404.2319])
        self.function_minimum_fitness = -959.6407
        self.dimensions = 2
        self.precision = 60
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        return -(x1 + 47) * np.sin(np.sqrt(np.absolute(x1 + (x0 / 2) + 47))) - x0 * np.sin(
            np.sqrt(np.absolute(x0 - (x1 + 47))))


class Sphere:
    def __init__(self):
        self.limits = np.array([-32, 32], dtype="int64")
        self.function_minimum = np.array([0, 0])
        self.function_minimum_fitness = 0
        self.dimensions = 2
        self.precision = 5
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        return x0**2 + x1**2


class Cross:
    def __init__(self):
        self.limits = np.array([-10, 10], dtype="int64")
        self.function_minimum = np.array([1.349407, 1.349407])
        self.dimensions = 2
        self.precision = 1
        self.rotation_number = 45

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        a = np.sqrt(x0 ** 2 + x1 ** 2) / np.pi
        b = np.exp(np.absolute(100 - a))
        c = np.sin(x0) * np.sin(x1) * b
        d = (np.absolute(c) + 1) ** 0.1
        return -0.0001 * d


class Booth:
    def __init__(self):
        self.limits = np.array([-10, 10], dtype="int64")
        self.function_minimum = np.array([1, 3])
        self.function_minimum_fitness = 0
        self.dimensions = 2
        self.precision = 1
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        return (x0+2*x1-7)**2+(2*x0+x1-5)**2


class Easom:
    def __init__(self):
        self.limits = np.array([-100, 100], dtype="int64")
        self.function_minimum = np.array([np.pi, np.pi])
        self.function_minimum_fitness = -1
        self.dimensions = 2
        self.precision = 1
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        return -np.cos(x0)*np.cos(x1)*np.exp(-1*((x0-np.pi)**2+(x1-np.pi)**2))


class Schaffer2:
    def __init__(self):
        self.limits = np.array([-100, 100], dtype="int64")
        self.function_minimum = np.array([0, 0])
        self.function_minimum_fitness = 0
        self.dimensions = 2
        self.precision = 5
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        num = (np.sin(x0 ** 2 - x1 ** 2)) ** 2 - 0.5
        den = (1 + 0.001 * (x0 ** 2 + x1 ** 2)) ** 2
        return 0.5 + (num / den)


class Ellipse:
    def __init__(self):
        self.limits = np.array([-100, 100], dtype="int64")
        self.function_minimum = np.array([0, 0])
        self.function_minimum_fitness = 0
        self.dimensions = 2
        self.precision = 1
        self.rotation_number = 0

    def result(self, x):
        theta = np.radians(self.rotation_number)
        x0 = rotate_x(x[0], x[1], theta)
        x1 = rotate_y(x[0], x[1], theta)
        semiMajor = 0.000076
        semiMinor = 0.000001
        xt = x0 / semiMajor
        yt = x1 / semiMinor
        return np.sqrt(xt * xt + yt * yt)
'''
def beale(x,swarm):
    swarm.limits= np.array([-4.5,4.5],dtype="int64")
    swarm.function_minimum= np.array([3,0.5])
    return ((1.5-x[0]+x[0]*x[1])**2)+((2.25-x[0]+x[0]*x[1]**2)**2)+((2.625-x[0]+x[0]*x[1]**3)**2)

def ackley(x,swarm):
    swarm.limits= np.array([-32,32],dtype="int64")
    swarm.function_minimum= np.array([0,0])
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum_sq_term = -a * np.exp(-b * np.sqrt(x[0]*x[0] + x[1]*x[1]) / 2)
    cos_term = -np.exp((np.cos(c*x[0]) + np.cos(c*x[0])) / 2)
    return a + np.exp(1) + sum_sq_term + cos_term



def schaffer2(x,swarm):
    swarm.limits= np.array([-100,100],dtype="int64")
    swarm.function_minimum= np.array([0,0])
    num= (np.sin(x[0]**2-x[1]**2))**2-0.5
    den= (1+0.001*(x[0]**2+x[1]**2))**2
    return 0.5+(num/den)

def rastrigin(x,swarm):
    swarm.limits= np.array([-5.12,5.12],dtype="int64")
    swarm.function_minimum= np.array([0,0])

    return 20+(x[0]**2-10*np.cos(2*np.pi*x[0]))+(x[1]**2-10*np.cos(2*np.pi*x[1]))
'''
