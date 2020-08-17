import numpy as np


class Bukin6:
    def __init__(self):
        self.limits = np.array([-15, 3], dtype="int64")
        self.function_minimum = np.array([-10, 1])
        self.dimensions = 2
        self.precision = 0.5

    def result(self, x):
        return 100 * (np.sqrt(np.absolute(x[1] - 0.01 * x[0] ** 2))) + (0.01 * np.absolute(x[0] + 10))


class Eggholder:
    def __init__(self):
        self.limits = np.array([-512, 512], dtype="int64")
        self.function_minimum = np.array([512, 404.2319])
        self.dimensions = 2
        self.precision = 60

    def result(self, x):
        return -(x[1] + 47) * np.sin(np.sqrt(np.absolute(x[1] + (x[0] / 2) + 47))) - x[0] * np.sin(
            np.sqrt(np.absolute(x[0] - (x[1] + 47))))


class Sphere:
    def __init__(self):
        self.limits = np.array([-32, 32], dtype="int64")
        self.function_minimum = np.array([0, 0])
        self.dimensions = 2
        self.precision = 5

    def result(self, x):
        return x[0]**2 + x[1]**2


class Cross:
    def __init__(self):
        self.limits = np.array([-10, 10], dtype="int64")
        self.function_minimum = np.array([1.349407, 1.349407])
        self.dimensions = 2
        self.precision = 1

    def result(self, x):
        a = np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi
        b = np.exp(np.absolute(100 - a))
        c = np.sin(x[0]) * np.sin(x[1]) * b
        d = (np.absolute(c) + 1) ** 0.1
        return -0.0001 * d


'''
def booth(x,swarm):
    swarm.limits= np.array([-10,10],dtype="int64")
    swarm.function_minimum= np.array([1,3])
    return (x[0]+2*x[1]-7)**2+(2*x[0]+x[1]-5)**2

def beale(x,swarm):
    swarm.limits= np.array([-4.5,4.5],dtype="int64")
    swarm.function_minimum= np.array([3,0.5])
    return ((1.5-x[0]+x[0]*x[1])**2)+((2.25-x[0]+x[0]*x[1]**2)**2)+((2.625-x[0]+x[0]*x[1]**3)**2)

def easom(x,swarm):
    swarm.limits= np.array([-100,100],dtype="int64")
    swarm.function_minimum= np.array([np.pi,np.pi])
    return -np.cos(x[0])*np.cos(x[1])*np.exp(-1*((x[0]-np.pi)**2+(x[1]-np.pi)**2))


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
