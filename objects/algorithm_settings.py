class AlgorithmSettings:
    def __init__(self, iterations, particles_number, function, c1, c2, w, random_variable_method, modify_velocity):
        self.function = function
        self.iterations = iterations
        self.particles_number = particles_number
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.random_variable_method = random_variable_method
        self.iteration = 0
        self.modify_velocity = modify_velocity
