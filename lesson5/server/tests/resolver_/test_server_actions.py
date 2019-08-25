from resolver import get_server_actions
from echo.controllers import echo_controller


TEST_INSTALLED_APPS = [
    'echo'
]

EXPECTED_ACTION = 'echo'

EXPECTED_CONTROLLER = echo_controller


def test_get_server_actions():
    action_list = get_server_actions(TEST_INSTALLED_APPS)

    assert len(action_list) == 1
    assert action_list[0].get('action') == EXPECTED_ACTION
    assert action_list[0].get('controller') == EXPECTED_CONTROLLER