
from task_manager import health_check


def test_health_check():
    assert health_check() is True
