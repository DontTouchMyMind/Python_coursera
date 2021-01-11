import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.carrying = carrying
        self.photo_file_name = photo_file_name
        self.brand = brand

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            self.body_length, self.body_width, self.body_height = map(float, self.body_whl.split('x'))
        except ValueError:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        res = []
        for row in reader:
            print(row[0])
            # Преобразовать элементы в список (split(','))
            # Оценить значения для создания

    car_list = []

    return car_list     # Возвращает список созданных объектов.


get_car_list('_cars.csv')