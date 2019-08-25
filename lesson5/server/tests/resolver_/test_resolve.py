from resolver import resolve
from echo.controllers import echo_controller


TEST_ACTION = 'echo'
TEST_INSTALLED_APPS = [
    'echo'
]

EXPECTED_CONTROLLER = echo_controller

def test_resolve():
    action = resolve(TEST_ACTION, TEST_INSTALLED_APPS)

    assert action == EXPECTED_CONTROLLER