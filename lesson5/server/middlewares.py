import zlib
from functools import wraps


def compression_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        request_bytes = zlib.decompress(request)
        response_bytes = func(request_bytes, *args, **kwargs)
        return zlib.compress(response_bytes)
    return wrapper

