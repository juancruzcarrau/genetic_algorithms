from random import shuffle, randint

from classes.city import City
from classes.solution import Solution


def order_crossover(cities: list[City], solutions: list[Solution]):
    """
    Preforms Order Crossover (OX1) on the solutions, randomly choosing two solutions as parents,
    generating 2 new offspring solutions.
    Go to https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_crossover.htm for more information
    :param cities: list of cities
    :param solutions: list of solutions to be crossovered
    :return: list with offspring, same size as the solutions
    """

    # Create a random order in which to match the solutions.
    # Solution[order[i]] will be matched to Solution[order[i+1]]
    random_order = list(range(len(solutions)))
    shuffle(random_order)
    offspring = []

    for i in range(0, len(solutions), 2):
        solution_1 = solutions[random_order[i]]
        solution_2 = solutions[random_order[i+1]]

        cut_1 = randint(0, len(cities) - 1)
        while True:
            cut_2 = randint(0, (len(cities)) - 1)
            if cut_1 != cut_2:
                break
        first_cut = min(cut_1, cut_2)
        second_cut = max(cut_1, cut_2)

        new_order_1 = _order_crossover_calculator(solution_1.order, solution_2.order, first_cut, second_cut)
        new_order_2 = _order_crossover_calculator(solution_2.order, solution_1.order, first_cut, second_cut)
        offspring_1 = Solution(new_order_1)
        offspring_2 = Solution(new_order_2)
        offspring.append(offspring_1)
        offspring.append(offspring_2)

    return offspring


def _order_crossover_calculator(parent_1: list[int], parent_2: list[int], first_cut: int, second_cut: int) -> list[int]:
    length = len(parent_1)
    new_order = [0 for _ in range(length)]
    segment = parent_1[first_cut:second_cut]
    new_order[first_cut:second_cut] = segment

    i = second_cut % length  # pointer in new_order
    j = second_cut % length # pointer in parent_2
    for _ in range(length):
        if parent_2[j] not in segment:
            new_order[i] = parent_2[j]
            i = (i + 1) % length
        j = (j + 1) % length

    return new_order



