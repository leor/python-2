from echo.controllers import echo_controller
from protocol import make_response
from datetime import datetime


INITIAL_ACTION = 'echo'
INITIAL_DATA = 'Test'

INITIAL_REQUEST = {
    'action': INITIAL_ACTION,
    'data': INITIAL_DATA,
    'time': datetime.now().timestamp()
}

EXPECTED_CODE = 200
EXPECTED_RESPONSE = make_response(INITIAL_REQUEST, EXPECTED_CODE, INITIAL_DATA)


def test_echo_controller():
    response = echo_controller(INITIAL_REQUEST)

    assert response.get('code') == EXPECTED_CODE
    assert response.get('data') == INITIAL_DATA
    assert response.get('action') == INITIAL_REQUEST.get('action')
    assert 'time' in response
