import pytest
from datetime import datetime


from protocol import make_response


INITIAL_ACTION = 'test'

INITIAL_DATA = 'Test data'

INITIAL_CODE = 200

INITIAL_REQUEST = {
    'action': INITIAL_ACTION,
    'time': datetime.now().timestamp()
}


def test_make_response_action():
    result = make_response(INITIAL_REQUEST, INITIAL_CODE, INITIAL_DATA)
    assert result.get('action') == INITIAL_ACTION

def test_make_response_code():
    result = make_response(INITIAL_REQUEST, INITIAL_CODE, INITIAL_DATA)
    assert result.get('code') == INITIAL_CODE

def test_make_response_data():
    result = make_response(INITIAL_REQUEST, INITIAL_CODE, INITIAL_DATA)
    assert result.get('data') == INITIAL_DATA

def test_make_response_has_time():
    result = make_response(INITIAL_REQUEST, INITIAL_CODE, INITIAL_DATA)
    assert 'time' in result