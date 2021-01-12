import os
import csv
import sys


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if not all(i != '' for i in (brand, photo_file_name, carrying)):
            raise ValueError
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.check_photo = self.get_photo_file_ext()

    def get_photo_file_ext(self):
        if os.path.splitext(self.photo_file_name)[1] not in ['.jpg', '.jpeg', '.png', '.gif']:
            raise ValueError
        else:
            return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            self.body_length, self.body_width, self.body_height = map(float, self.body_whl.split('x'))
        except ValueError:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        if extra == '':
            raise ValueError
        else:
            self.extra = extra


def parse_data_cars(input_data: str) -> list:
    """Функция преобразует строку с данными в список."""
    return input_data.split(',')


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        for row in reader:
            try:
                vehicle = parse_data_cars(row[0])

                if vehicle[0] == 'car':
                    new_car = Car(vehicle[1], vehicle[3], vehicle[5], vehicle[2])
                elif vehicle[0] == 'truck':
                    new_car = Truck(vehicle[1], vehicle[3], vehicle[5], vehicle[4])
                elif vehicle[0] == 'spec_machine':
                    new_car = SpecMachine(vehicle[1], vehicle[3], vehicle[5], vehicle[6])
                else:
                    continue
            except (ValueError, TypeError):
                pass
            except IndexError:
                continue
            else:
                car_list.append(new_car)
    return car_list  # Возвращает список созданных объектов.


if __name__ == '__main__':
    print(get_car_list(sys.argv[1]))