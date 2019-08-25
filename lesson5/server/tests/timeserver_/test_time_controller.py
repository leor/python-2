from timeserver.controllers import time_controller
from protocol import make_response
from datetime import datetime


INITIAL_ACTION = 'server:time'

INITIAL_REQUEST = {
    'action': INITIAL_ACTION,
    'time': datetime.now().timestamp()
}

EXPECTED_CODE = 200
EXPECTED_RESPONSE = make_response(INITIAL_REQUEST, EXPECTED_CODE)


def test_time_controller():
    response = time_controller(INITIAL_REQUEST)

    assert response.get('code') == EXPECTED_CODE
    assert response.get('action') == INITIAL_REQUEST.get('action')
    assert 'time' in response
    assert 'data' in response
    assert type(response.get('data')) == float
