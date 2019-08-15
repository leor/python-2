import pytest
from servererror.controllers import error_controller
from datetime import datetime


INITIAL_ACTION = 'server:error'

INITIAL_REQUEST = {
    'action': INITIAL_ACTION,
    'time': datetime.now().timestamp()
}


def test_error_controller():
    with pytest.raises(Exception, match="Custom server error"):
        error_controller(INITIAL_REQUEST)