import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(prog='Travelling Salesman Problem')

    parser.add_argument('-p', '--population_size', type=int)
    parser.add_argument('-g', '--amount_of_generations', type=int)

    return parser.parse_args()
