from protocol import make_response
from datetime import datetime


def time_controller(request):
    return make_response(request, 200, datetime.now().timestamp())


def formated_date_controller(request):
    return make_response(request, 200, datetime.now().strftime('%Y-%m-%d %H:%M'))