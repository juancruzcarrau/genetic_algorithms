from itertools import count
from time import sleep

from classes.city import City
from classes.solution import Solution
from main import tsp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

if __name__ == '__main__':
    POPULATION_SIZE = 100
    AMOUNT_OF_GENERATIONS = 10000
    AMOUNT_OF_MUTATIONS = 4

    city1 = City("A", 1, 1)
    city2 = City("B", 1, 2)
    city3 = City("C", 2, 2)
    city4 = City("D", 3, 2)
    city5 = City("E", 3, 1)
    city6 = City("F", 2, 1)
    cities = [city1, city2, city3, city4, city5, city6]

    best_solution, best_solutions = tsp(cities, POPULATION_SIZE, AMOUNT_OF_GENERATIONS, AMOUNT_OF_MUTATIONS)
    my_solution = Solution([0, 1, 2, 3, 4, 5], cities)

    # Get the cities in order of the best solution
    cities_in_order = [cities[i] for i in best_solution.order]

    # Graph the solution
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

    latitudes = [city.lat for city in cities_in_order + [cities_in_order[0]]]
    longitudes = [city.long for city in cities_in_order + [cities_in_order[0]]]
    ax1.plot(longitudes, latitudes, '.-k')

    # Graph the fitness progression
    ax2.plot([solution.fitness for solution in best_solutions])

    # Show how solutions evolved
    counter = count()
    best_solutions_distinct = list(set(best_solutions))
    best_solutions_distinct.sort(key=lambda x: x.fitness, reverse=True)
    print(f"Amount of improvments: {len(best_solutions_distinct)}")


    def animate(i):
        index = next(counter)
        if index == best_solutions_distinct:
            sleep(5)
        cities_in_order = [cities[i] for i in best_solutions_distinct[index % len(best_solutions_distinct)].order]
        latitudes = [city.lat for city in cities_in_order]
        longitudes = [city.long for city in cities_in_order]

        ax3.cla()
        ax3.plot(longitudes, latitudes, '.-k')


    ani = FuncAnimation(plt.gcf(), animate, interval=20)
    plt.show()
