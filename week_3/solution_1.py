class FileReader:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def read(self):
        try:
            with open(self.path_to_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''

# РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ
# class FileReader:
#     """Класс FileReader помогает читать из файла"""
#
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def read(self):
#         try:
#             with open(self.file_path) as f:
#                 return f.read()
#         except IOError:
#             return ""
