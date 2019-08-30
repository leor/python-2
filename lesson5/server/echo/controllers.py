from protocol import make_response
from decorators import log


@log('%(name)s - %(result)s')
def echo_controller(request):
    return make_response(request, 200, request.get('data'))