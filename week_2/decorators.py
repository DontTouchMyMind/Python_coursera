import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrap
