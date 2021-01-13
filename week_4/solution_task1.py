import os
import tempfile


class File:

    def __init__(self, filename) -> None:
        self.filename = str(filename)
        self.file_path = os.path.join(tempfile.gettempdir(), self.filename)
        self.file_data = self.read_data_from_file()

    def read_data_from_file(self) -> list:
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w+') as f:
                f.write('')
            return ['']
        else:
            with open(self.file_path, 'r') as f:
                return f.readlines()

    def __str__(self) -> str:
        """Возвращать полный путь до файла"""
        return self.file_path

    def __add__(self, other) -> 'File':
        """Содержимое второго файла добавляется к содержимому первого файла"""
        new_file = File(tempfile.NamedTemporaryFile())
        new_file.write(self.read() + other.read())
        return new_file

    def read(self) -> str:
        """Метод чтения из файла"""
        with open(self.file_path, 'r') as f:
            return f.read()

    def write(self, data: str) -> int:
        """Метод записи в файл"""
        with open(self.file_path, 'w') as f:
            f.writelines(data)
        return len(data)

    def __iter__(self):
        yield from open(self.file_path)

    def __next__(self):
        row_counter = 0
        with open(self.file_path, 'r') as f:
            current_row = f.readlines()[row_counter]
        row_counter += 1
        if current_row == '':
            raise StopIteration
        return current_row

# SOLUTION FROM TEACHER
# import os
# import uuid
#
#
# class File:
#     def __init__(self, path):
#         self.path = path
#         self.current_position = 0
#
#         if not os.path.exists(self.path):
#             open(self.path, 'w').close()
#
#     def write(self, content):
#         with open(self.path, 'w') as f:
#             return f.write(content)
#
#     def read(self):
#         with open(self.path, 'r') as f:
#             return f.read()
#
#     def __add__(self, obj):
#         new_path = os.path.join(
#             os.path.dirname(self.path),
#             str(uuid.uuid4().hex)
#         )
#         new_file = type(self)(new_path)
#         new_file.write(self.read() + obj.read())
#
#         return new_file
#
#     def __str__(self):
#         return self.path
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         with open(self.path, 'r') as f:
#             f.seek(self.current_position)
#
#             line = f.readline()
#             if not line:
#                 self.current_position = 0
#                 raise StopIteration('EOF')
#
#             self.current_position = f.tell()
#             return line
#
