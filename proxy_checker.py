import requests

def test_proxy(proxy):
    try:
        response = requests.get("http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
        return response.status_code == 200
    except:
        return False

def filter_working_proxies(proxy_list):
    print("🔍 Testando proxies...")
    working = [p for p in proxy_list if test_proxy(p)]
    print(f"✅ {len(working)} proxies válidos encontrados.")
    return working
