from proxy_sources import fetch_proxies
from proxy_checker import filter_working_proxies

def update_proxy_list():
    proxies = fetch_proxies()
    valid = filter_working_proxies(proxies)
    with open("proxies.txt", "w") as f:
        f.write('\n'.join(valid))

if __name__ == "__main__":
    update_proxy_list()
