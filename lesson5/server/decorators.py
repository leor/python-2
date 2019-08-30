import logging
from functools import wraps

from protocol import make_response


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


def authorized(func):
    @wraps(func)
    def wrapper(request):
        if request.get('token'):
            return func(request)
        else:
            return make_response(request, 401, 'Access denied')
    return wrapper