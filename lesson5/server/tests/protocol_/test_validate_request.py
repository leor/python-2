from datetime import datetime


from protocol import validate_request


INITIAL_ACTION = 'test'

INITIAL_REQUEST = {
    'action': INITIAL_ACTION,
    'time': datetime.now().timestamp()
}

BAD_REQUESTS = [
    {
        'action': INITIAL_ACTION,
    },
    {
        'time': datetime.now().timestamp(),
    },
    {}
]


def test_correct_request():
    assert validate_request(INITIAL_REQUEST) == True

def test_bad_requests():
    for bad_request in BAD_REQUESTS:
        assert validate_request(bad_request) == False