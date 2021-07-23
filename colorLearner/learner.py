import pygad
import sys

from color_squares import ColorSquares
from textwrap import wrap

def hex_to_rgb(hex_int):
    hex_strings = wrap(hex(hex_int)[2:])
    return [int(rgb_string, 16) for hex_string in hex_strings for rgb_string in wrap(hex_string, 2)]

def deflatten(solution, total_rows, row_width):
    deflattened = []
    next_item = 0
    for _ in range(total_rows):
        deflattened.append([])
        for _ in range(row_width):
            deflattened[-1].append(solution[next_item])
            next_item += 1
    
    return deflattened

def get_fitness(solution, solution_indx, displayer, height, width):
    rgb_values = [hex_to_rgb(hex_value) for hex_value in solution]
    if any([len(rgb_value) != 3 for rgb_value in rgb_values]) or any([r not in range(0, 256) or g not in range(0, 256) or b not in range(0, 255) for r, g, b in rgb_values]):
        return -1

    deflattened = deflatten(rgb_values, height, width)

    displayer.update_squares(deflattened)

    return float(input("Give a fitness to this grid (higher is better): "))

if __name__ == "__main__":

    if len(sys.argv) == 2:
        squares_height = int(sys.argv[1])
    else:
        squares_height = 15
        squares_width = 15
    
    square_displayer = ColorSquares([])
    learner = pygad.GA( num_generations=50,
                        num_parents_mating=4,
                        num_genes=squares_height * squares_height,
                        fitness_func=lambda solution, index: get_fitness(solution, index, square_displayer, squares_height, squares_width),
                        gene_type=int,
                        init_range_low=0,
                        sol_per_pop=10,
                        init_range_high=16777215)

    square_displayer.update_squares(learner.population[0])

    square_displayer.start()
    
    learner.run()

