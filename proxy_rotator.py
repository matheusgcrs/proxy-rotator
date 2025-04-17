import random

def get_proxy():
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        return random.choice(proxies)
    except FileNotFoundError:
        print("❌ Nenhuma lista de proxies encontrada.")
        return None
