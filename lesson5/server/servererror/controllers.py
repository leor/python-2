from protocol import make_response
from decorators import log, authorized


@authorized
@log('%(name)s')
def error_controller(request):
    raise Exception('Custom server error')