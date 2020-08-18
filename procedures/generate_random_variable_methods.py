import numpy as np


def rotationally_variant(dimensions):
    r = np.random.uniform(0, 1, dimensions)
    return r


def rotationally_invariant(dimensions):
    r = np.random.uniform(0, 1)
    return r
