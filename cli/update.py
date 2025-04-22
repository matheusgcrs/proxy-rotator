from core.sources import fetch_proxies
from core.checker import filter_working_proxies
from core.enricher import enrich_proxy_list
from pprint import pprint

def main():
    proxies = fetch_proxies()
    valid = filter_working_proxies(proxies)
    enriched = enrich_proxy_list(valid)
    pprint(enriched)

if __name__ == "__main__":
    main()
