import requests

# Функция которая возвращает текущий ip компьютера
def get_ip():
    return requests.get("https://ipinfo.io/ip").text

def get_updates(only_last:bool = False, game_id = ""):
    news = requests.get(f"http://127.0.0.1:8000/updates/{game_id}").json()
    if only_last:
        return news[0]
    return news
