import csv
import os

from classes.city import City


class CitiesProvider:
    _csv_file_path = os.path.dirname(__file__) + "/../../csv/uscities_100.csv"

    @staticmethod
    def provide():
        cities = []
        with open(CitiesProvider._csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader)  # skip header
            for row in csv_reader:
                name = row[1]
                lat = float(row[6].replace(',', '.'))
                long = float(row[7].replace(',', '.'))
                cities.append(City(name, lat, long))
        return cities
