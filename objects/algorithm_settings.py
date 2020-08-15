class GeneticAlgorithm:
    def __init__(self, iterations, particles_number, function, angle, cross_chance, radius_limit):
        self.function = function
        self.iterations = iterations
        self.particles_number = particles_number
