import os
import pickle

from main import plot_results
from providers.csv_provider import CitiesProvider

if __name__ == '__main__':
    best_solution = None
    best_solutions = None

    file_path_root = os.path.dirname(__file__) + f"/../../Results (binary)/05-Dec-2022 - 14-27-00 - 100 - 1000/"

    with open(file_path_root + 'best_solution', 'rb') as f:
        best_solution = pickle.load(f)

    with open(file_path_root + 'best_solutions', 'rb') as f:
        best_solutions = pickle.load(f)

    cities = CitiesProvider.provide()
    plot_results(cities, best_solution, best_solutions)