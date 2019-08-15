from protocol import make_response


def error_controller(request):
    raise Exception('Custom server error')