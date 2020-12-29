import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrap


# Solution from the teacher
#
# import functools
# import json
#
#
# def to_json(func):
#
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return json.dumps(result)
#
#     return wrapped
