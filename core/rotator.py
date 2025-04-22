from core.models import Proxy

class ProxyRotator:
    def __init__(self, proxies: list[Proxy]):
        self.proxies = proxies
        self.index = 0

    def get_next(self) -> Proxy:
        if not self.proxies:
            raise ValueError("Proxy list is empty.")
        proxy = self.proxies[self.index]
        self.index = (self.index + 1) % len(self.proxies)
        return proxy