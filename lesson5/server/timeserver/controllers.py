from protocol import make_response
from datetime import datetime
from decorators import log


@log('%(name)s - %(result)s')
def time_controller(request):
    return make_response(request, 200, datetime.now().timestamp())


@log('%(name)s - %(result)s')
def formated_date_controller(request):
    return make_response(request, 200, datetime.now().strftime('%Y-%m-%d %H:%M'))