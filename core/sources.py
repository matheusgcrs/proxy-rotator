import requests
from core.models import Proxy

def fetch_proxies() -> list[Proxy]:
    print("Buscando proxies de múltiplas fontes...")
    urls = [
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=3000&country=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://www.proxy-list.download/api/v1/get?type=http"
    ]

    proxies = set()
    for url in urls:
        try:
            print(f"Buscando de: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            for line in response.text.strip().splitlines():
                if ":" in line:
                    ip, porta = line.strip().split(":")
                    proxies.add(Proxy(ip, porta))
        except Exception as e:
            print(f"Erro ao buscar de {url}: {e}")

    print(f"Total de {len(proxies)} proxies coletados.")
    return list(proxies)
