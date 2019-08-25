from timeserver.controllers import formated_date_controller
from protocol import make_response
from datetime import datetime


INITIAL_ACTION = 'server:formatted'

INITIAL_REQUEST = {
    'action': INITIAL_ACTION,
    'time': datetime.now().timestamp()
}

EXPECTED_CODE = 200
EXPECTED_RESPONSE = make_response(INITIAL_REQUEST, EXPECTED_CODE)


def test_formated_date_controller():
    response = formated_date_controller(INITIAL_REQUEST)

    assert response.get('code') == EXPECTED_CODE
    assert response.get('action') == INITIAL_REQUEST.get('action')
    assert 'time' in response
    # не самый удачный тест :)
    assert response.get('data') == datetime.now().strftime('%Y-%m-%d %H:%M')
