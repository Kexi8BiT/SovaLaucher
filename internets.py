import requests

# Функция которая возвращает текущий ip компьютера
def get_ip():
    return requests.get("https://ipinfo.io/ip").text



# Эта функция возвращает обнавления указанной игры
def get_updates(only_last:bool = False, game_id = "") -> []:
    news = requests.get(f"http://127.0.0.1:8000/updates/{game_id}").json()
    if only_last:
        return news[0]
    return news


#Функция для проверки работы нового api (пока что только существование потом добавлю проверку всех ендпоинтов)
def check_api(url: str) -> bool:
    """
    Функция для проверки работы нового api
    ```python
        check_api("http://127.0.0.1:8000") -> Fasle/TRue
    ```
    :param url:
    :return:
    """
    try:
        req = requests.get(f"{url}/online")
        if req.status_code == 200:
            req_json = req.json()
            print(req_json)
            if "status" in req_json:
                print("API работает")
                return True

            else:
                print("в json нет online")
                return False
        else:
            print("не 200")
            return False
    except Exception as e:
        print(e)
        return False
