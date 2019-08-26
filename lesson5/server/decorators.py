import logging
from functools import wraps


logger = logging.getLogger('server')


def log(format):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.debug(format % {'name': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result})
            
            return result
        return wrapper
    return decorator