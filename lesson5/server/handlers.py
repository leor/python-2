import json
import logging

from resolver import resolve
from protocol import make_response, validate_request
from middlewares import compression_middleware

from settings import INSTALLED_APPS


@compression_middleware
def handle_tcp_request(client_bytes):
    request = json.loads(client_bytes.decode())

    if(validate_request(request)):
        action = request.get('action')
        controller = resolve(action, INSTALLED_APPS)

        if controller:
            try:
                response = controller(request)
                logging.info(f'Sending server response {response}')
            except Exception as err:
                response = make_response(request, 500, 'Internal server error')
                logging.critical(f'Exception - {err}')    
        else:
            response = make_response(request, 404, f'Action {action} not found')
            logging.error(f'Client call unknown action {action}')
    else:
        response = make_response(request, 400, 'Wrong request')
        logging.error(f'Client sent wrong request {request}')

    return json.dumps(response).encode()

