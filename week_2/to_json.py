import json
from decorators import to_json


@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data())


@to_json
def get_int():
    return 2


print(get_int())


@to_json
def get_list():
    return [2]


print(get_list())


@to_json
def get_tuple():
    return tuple(("python", "json", "mysql"))


print(get_tuple())


@to_json
def get_str():
    return "test"


print(get_str())


@to_json
def get_float():
    return 3.4


print(get_float())
