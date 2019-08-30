from datetime import datetime
from decorators import log


@log('%(name)s%(args)s - %(result)s')
def validate_request(request):
    return 'action' in request and 'time' in request

@log('%(name)s%(args)s - %(result)s')
def make_response(request, code, data=None):
    return {
        'code': code,
        'action': request.get('action'),
        'data': data, 
        'time': datetime.now().timestamp(),
    }
