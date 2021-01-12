import csv
import sys
import os.path


class CarBase:
    """Базовый класс с общими методами и атрибутами"""

    def __init__(self, brand, photo_file_name, carrying):
        # проверка что аргументы не являются пустой строкой
        if not all(i != '' for i in (brand, photo_file_name, carrying)):
            raise ValueError

        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        # вызов метода для проверки расширения файла изображения
        self.ext = self.get_photo_file_ext()

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        if ext not in ['.jpg', '.jpeg', '.png', '.gif']:
            raise ValueError
        return ext


class Car(CarBase):
    """Класс легковой автомобиль"""

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    """Класс грузовой автомобиль"""

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        # обрабатываем поле body_whl
        try:
            length, width, height = (float(c) for c in body_whl.split('x', 2))
        except ValueError:
            length, width, height = .0, .0, .0

        self.body_length = length
        self.body_width = width
        self.body_height = height

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    """Класс спецтехника"""

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        # проверка что аргумент extra не является пустой строкой
        if extra == '':
            raise ValueError
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename, encoding='utf-8') as csv_fd:
        # создаем объект csv.reader для чтения csv-файла
        reader = csv.reader(csv_fd, delimiter=';')

        # пропускаем заголовок csv
        next(reader)

        # это наш список, который будем возвращать
        car_list = []

        # объявим словарь, ключи которого - тип автомобиля (car_type),
        # а значения - функция, создающая экземпляр нужного класса
        car_types = {
            'car': lambda x: Car(x[1], x[3], x[5], x[2]),
            'truck': lambda x: Truck(x[1], x[3], x[5], x[4]),
            'spec_machine': lambda x: SpecMachine(x[1], x[3], x[5], x[6])}

        # обрабатываем csv-файл построчно
        for row in reader:
            try:
                car_type = row[0]
                # если тип машины в словаре - создаем экземпляр класса
                if car_type in car_types:
                    car_list.append(car_types[car_type](row))
            # при возникновении ошибки - пропускаем строку
            except (ValueError, IndexError):
                pass

    return car_list


if __name__ == '__main__':
    print(get_car_list(sys.argv[1]))

