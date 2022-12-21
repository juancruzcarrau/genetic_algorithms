from math import sqrt
from random import randint
from random import random

from classes.city import City


class Solution:

    def __init__(self, order: list[int]):
        self.order = order
        self.fitness = None

    def calculate_fitness(self, cities: list[City]):
        total_distance = 0
        i = 0
        while i < len(cities):
            first_city = cities[self.order[i]]
            second_city = cities[self.order[(i + 1) % len(cities)]]
            distance = Solution._euclidean_distance(first_city.lat - second_city.lat,
                                                    first_city.long - second_city.long)

            total_distance += distance
            i += 1

        self.fitness = total_distance

    @staticmethod
    def _euclidean_distance(x: float, y: float) -> float:
        return sqrt((x ** 2) + (y ** 2))

    def __gt__(self, other):
        return self.fitness < other.fitness

    def __eq__(self, other):
        return self.order == other.order

    def __hash__(self):
        return int(''.join([str(i) for i in self.order]))

    def mutate(self, cities: list[City], probability_of_mutation):
        if probability_of_mutation < random():
            first_city = randint(0, len(self.order) - 1)
            while True:
                second_city = randint(0, len(self.order) - 1)
                if first_city != second_city:
                    break
            self.order[first_city], self.order[second_city] = self.order[second_city], self.order[first_city]

        self.calculate_fitness(cities)
