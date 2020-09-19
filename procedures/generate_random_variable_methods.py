import numpy as np


def rotationally_variant(dimensions):
    r = np.random.uniform(0, 1, dimensions)
    return r


def hybrid(dimensions):
    r = np.zeros(dimensions, dtype='float64')
    r[0] = np.random.uniform(0, 1)
    r[1] = np.random.normal(r[0], 0.01)
    return r


def rotationally_invariant(dimensions):
    r = np.random.uniform(0, 1)
    return r
