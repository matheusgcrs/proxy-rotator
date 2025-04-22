import pytest
from core.models import Proxy
from core.rotator import ProxyRotator

def test_rotator_cycles():
    proxies = [Proxy("1.1.1.1", "8080"), Proxy("2.2.2.2", "8080")]
    rotator = ProxyRotator(proxies)

    assert str(rotator.get_next()) == "1.1.1.1:8080"
    assert str(rotator.get_next()) == "2.2.2.2:8080"
    assert str(rotator.get_next()) == "1.1.1.1:8080"


def test_rotator_empty():
    with pytest.raises(ValueError):
        rotator = ProxyRotator([])
        rotator.get_next()
