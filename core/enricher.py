import requests
from core.models import Proxy, EnrichedProxy

def get_proxy_location(ip: str) -> dict:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        if response.get("status") == "success":
            return {
                "pais": response.get("country", ""),
                "regiao": response.get("regionName", ""),
                "cidade": response.get("city", "")
            }
    except:
        pass
    return {"pais": "", "regiao": "", "cidade": ""}

def enrich_proxy_list(proxies: list[Proxy]) -> list[EnrichedProxy]:
    print("Adicionando localização aos proxies...")
    enriched = []

    for proxy in proxies:
        location = get_proxy_location(proxy.ip)
        enriched.append(EnrichedProxy(
            ip=proxy.ip,
            porta=proxy.porta,
            pais=location["pais"],
            regiao=location["regiao"],
            cidade=location["cidade"]
        ))

    print(f"{len(enriched)} proxies localizados.")
    return enriched