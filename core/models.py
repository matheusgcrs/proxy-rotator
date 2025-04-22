from dataclasses import dataclass

@dataclass(frozen=True)
class Proxy:
    ip: str
    porta: str

    def __str__(self):
        return f"{self.ip}:{self.porta}"

@dataclass(frozen=True)
class EnrichedProxy(Proxy):
    pais: str = ""
    regiao: str = ""
    cidade: str = ""