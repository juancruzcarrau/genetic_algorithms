from random import shuffle

from classes.solution import Solution


def tournament_selection(solutions: list[Solution]):
    """
    Function that given a list of solutions, pairs them randomly and preforms a tournament selection
    :param solutions: list of solutions to the TSP problem
    :return: the winning solutions after tournament selection
    """

    # Create a random order in which to compare the solutions.
    # Solution[order[i]] will be compared to Solution[order[i+1]]
    random_order = list(range(len(solutions)))
    shuffle(random_order)
    winners = []
    for i in range(0, len(solutions), 2):
        solution_1 = solutions[random_order[i]]
        solution_2 = solutions[random_order[i+1]]
        winner = solution_1 if solution_1 > solution_2 else solution_2
        winners.append(winner)
    return winners
