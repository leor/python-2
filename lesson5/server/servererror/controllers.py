from protocol import make_response
from decorators import log


@log('%(name)s')
def error_controller(request):
    raise Exception('Custom server error')