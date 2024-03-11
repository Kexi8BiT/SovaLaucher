import requests

# Функция которая возвращает текущий ip компьютера
def get_ip():
    return requests.get("https://ipinfo.io/ip").text

def get_updates(only_last:bool = False, game_id = ""):
    iohfvhjkhj = """
SovaDash исправил в себе несколько багов, и появились обновления:
- Скорость загрузки повысилось
- Добавлен Мультиплеер
- Исправлен редактор
- Добавлена нейронная сеть для редактирования уровней и отображения карты"""
    news = [
        {"name": "Зимнее обновление",
         "version": "1.2",
         "text": iohfvhjkhj,
         "date": "2023.02.20"},
        {"name": "Сервер создался!",
         "version": "1.0",
         "text": "Наконец - то SovaDash появился на прилавках SovaLauncher, в этой игре есть много всего, но самое крутое - это же святое!",
         "date": "2022.10.10"},
        {"name": "Сервер создался!",
         "version": "1.0",
         "text": "Наконец - то SovaDash появился на прилавках SovaLauncher, в этой игре есть много всего, но самое крутое - это же святое!",
         "date": "2022.10.10"},
        {"name": "Сервер создался!",
         "version": "1.0",
         "text": "Наконец - то SovaDash появился на прилавках SovaLauncher, в этой игре есть много всего, но самое крутое - это же святое!",
         "date": "2022.10.10"}
            ]
    if only_last:
        return news[0]
    return news