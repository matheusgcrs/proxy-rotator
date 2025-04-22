import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.models import Proxy

def test_proxy(proxy: Proxy) -> bool:
    try:
        proxy_str = str(proxy)
        response = requests.get(
            "https://api.ipify.org?format=json",
            proxies={"http": proxy_str, "https": proxy_str},
            timeout=5
        )
        return response.status_code == 200
    except:
        return False

def filter_working_proxies(proxies: list[Proxy], max_threads: int = None) -> list[Proxy]:
    if not proxies:
        print("Lista de proxies vazia.")
        return []

    if max_threads is None:
        max_threads = min(len(proxies), os.cpu_count() * 5)

    print(f"Testando {len(proxies)} proxies com até {max_threads} threads...")
    valid = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(test_proxy, proxy): proxy for proxy in proxies}
        for future in as_completed(futures):
            proxy = futures[future]
            try:
                if future.result():
                    valid.append(proxy)
            except:
                continue

    print(f"{len(valid)} proxies válidos encontrados.")
    return valid
