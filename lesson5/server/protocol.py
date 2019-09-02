from datetime import datetime


def validate_request(request):
    return 'action' in request and 'time' in request

def make_response(request, code, data=None):
    return {
        'code': code,
        'action': request.get('action'),
        'data': data, 
        'time': datetime.now().timestamp(),
    }
