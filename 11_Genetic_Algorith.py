# these practical asked in exam

import pygad
import numpy as np

X=[4,-2,3.5,5,-11,-4.7]
desired_output=44

def fitness_function(ga_instance, solution, solution_idx):
    output=np.sum(solution*X)# Output is the predicted output
    fitness=1.0/np.abs(output-desired_output) # we are trying to find error # fitness is reciprocal of error because we want to get a higher value return fitness
    return fitness

# ga_instance is a genetic algorithm instance
# solution
# Solution_index because there will be solutions for different generations,
ga_instance=pygad.GA(num_generations=50, #it will run 50 times
            num_parents_mating=8, # 8 parents will be used for cre
            fitness_func=fitness_function,
            sol_per_pop=8,# Solution_per_population
            # In each generation we will consider 8 childs as pare
            num_genes=len(X),
            init_range_low=-2,
            init_range_high=5,
            parent_selection_type="sss", #sss = Steady Selection St
            #It is for maintaining the same number of parents in e
            keep_parents=1, # Means that 1 parent from previous gen
            crossover_type="single_point",
            mutation_type="random",
            mutation_percent_genes=10
        ) 

ga_instance.run()
solution, solution_fitness, solution_idx=ga_instance.best_solution()

print("solution = ", solution)
print("Fitness = ", solution_fitness)
print("solution IDX = ", solution_idx)
