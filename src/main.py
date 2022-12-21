import argparse
import os
import pickle
import random
from datetime import timedelta, datetime
from itertools import count
from time import time, sleep

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from classes.city import City
from classes.solution import Solution
from functions.crossover_methods import order_crossover
from functions.selection_methods import tournament_selection
from parsers.parser import parse_arguments
from providers.csv_provider import CitiesProvider
from providers.alternative_provider import AlternativeProvider


def tsp(cities: list[City], population_size: int, amount_of_generations: int, probability_of_mutation: float):
    # Step 1: generate initial population
    population = [Solution(random.sample(range(len(cities)), len(cities))) for _ in range(population_size)]
    for solution in population:
        solution.calculate_fitness(cities)
    best_solutions = []
    times = []

    # Step 2: run the generations loop
    for generation in range(amount_of_generations):
        start_time = time()

        # Step 2.1: selection of surviving population
        survivors = tournament_selection(population)

        # Step 2.2: crossover with survivors
        offspring = order_crossover(cities, survivors)

        # Step 2.3: mutate the offspring
        for new_solution in offspring:
            new_solution.mutate(cities, probability_of_mutation)

        # Step 2.4: define the new population and run the loop again
        population = survivors + offspring

        best_solutions.append(min(population, key=lambda solution: solution.fitness))
        end_time = time()
        times.append(end_time - start_time)
        remaining_time = (amount_of_generations - generation) * (sum(times) / len(times))
        print(f"Generation {generation} | Remaining time - {timedelta(seconds=remaining_time)}")

    return best_solutions[-1], best_solutions


def plot_results(cities, best_solution, best_solutions):
    # Get the cities in order of the best solution
    cities_in_order = [cities[i] for i in best_solution.order] + [cities[best_solution.order[0]]]
    # Graph the solution
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    latitudes = [city.lat for city in cities_in_order]
    longitudes = [city.long for city in cities_in_order]
    ax1.title.set_text("Best solution")
    ax1.plot(longitudes, latitudes, '.-k')

    # Graph the fitness progression
    ax2.title.set_text(f"Fitness progresion\n(best = {best_solutions[-1].fitness})")
    ax2.plot([solution.fitness for solution in best_solutions])
    # Show how solutions evolved
    counter = count()
    best_solutions_distinct = list(set(best_solutions))
    best_solutions_distinct.sort(key=lambda x: x.fitness, reverse=True)
    print(f"Amount of improvments: {len(best_solutions_distinct)}")

    def animate(i):
        index = next(counter)
        if index % len(best_solutions_distinct) == 0 and index != 0:
            sleep(3)
        cities_in_order = [cities[i] for i in best_solutions_distinct[index % len(best_solutions_distinct)].order] \
                          + [cities[best_solutions_distinct[index % len(best_solutions_distinct)].order[0]]]
        latitudes = [city.lat for city in cities_in_order]
        longitudes = [city.long for city in cities_in_order]

        ax3.cla()
        ax3.title.set_text(f"Amount of improvements = {len(best_solutions_distinct)}")
        ax3.plot(longitudes, latitudes, '.-k')

    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    plt.tight_layout()
    plt.show()


def save_data(best_solution, best_solutions, population_size, amount_of_generations):
    current_date = datetime.now().strftime("%d-%b-%Y - %H-%M-%S")
    file_path_root = os.path.dirname(__file__) + f"/../../Results (binary)/{current_date} - {population_size} - {amount_of_generations} - {probability_of_mutation}/"

    os.makedirs(os.path.dirname(file_path_root), exist_ok=True)

    with open(file_path_root + "best_solution", 'wb') as f:
        pickle.dump(best_solution, f)

    with open(file_path_root + "best_solutions", 'wb') as f:
        pickle.dump(best_solutions, f)


if __name__ == '__main__':

    args = parse_arguments()

    population_size = args.population_size
    amount_of_generations = args.amount_of_generations
    probability_of_mutation = args.probability_of_mutation

    # cities = CitiesProvider.provide()
    cities = AlternativeProvider.provide()
    best_solution, best_solutions = tsp(cities, population_size, amount_of_generations, probability_of_mutation)
    save_data(best_solution, best_solutions, population_size, amount_of_generations)
    plot_results(cities, best_solution, best_solutions)
