import os
import csv

from dataclasses import dataclass


@dataclass
class CarProperties:
    car_type: str
    brand: str
    passenger_seats_count: str
    photo_file_name: str
    body_whl: str
    carrying: str
    extra: str


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


def parse_data_cars(input_data: str) -> CarProperties:
    """Функция преобразует строку с данными в объект."""
    return CarProperties(*input_data.split(','))


def check_car_base_data(obj):
    pass


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        for row in reader:
            vehicle = parse_data_cars(row[0])

            # Определить тип машины для создания
            if vehicle.car_type == 'car':
                print(f'{vehicle.car_type} {vehicle.passenger_seats_count}')
                # Проверить данные для создания объекта
                if vehicle.brand and vehicle.photo_file_name and vehicle.carrying and vehicle.passenger_seats_count:
                    # Создать объект
                    new_car = Car(vehicle.brand,
                                  vehicle.photo_file_name,
                                  vehicle.carrying,
                                  vehicle.passenger_seats_count)
                    # Добавить объект к списку
                    car_list.append(new_car)

            elif vehicle.car_type == 'truck':
                print(f'{vehicle.car_type} {vehicle.body_whl}')
                if vehicle.brand and vehicle.photo_file_name and vehicle.carrying:
                    new_car = Truck(vehicle.brand,
                                    vehicle.photo_file_name,
                                    vehicle.carrying,
                                    vehicle.body_whl)
                    car_list.append(new_car)
                pass
            elif vehicle.car_type == 'spec_machine':
                print(f'{vehicle.car_type} {vehicle.extra}')
                if vehicle.brand and vehicle.photo_file_name and vehicle.carrying and vehicle.extra:
                    new_car = Truck(vehicle.brand,
                                    vehicle.photo_file_name,
                                    vehicle.carrying,
                                    vehicle.extra)
                    car_list.append(new_car)
            else:
                # print('Error parameters')
                pass
    # print(car_list)
    return car_list  # Возвращает список созданных объектов.


# get_car_list('_cars.csv')
