import hashlib
import os
import requests

def file_hash_(file_path: str) -> str:
    """
    Возвращает md5 hash файла по его пути
    ```python
    path = "/path/to/file.txt"
    hash_md5 = file_hash(path)
    print(hash_md5)
    ```
    :param file_path:
    :return:
    """
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except:
        return "404"


def is_directory(path: str) -> bool:
    return os.path.isdir(path)
def files_update(path_to_games_dir: str, game_id: str, files_hashs) -> None:
    error_files = []
    file_names = []
    for file in files_hashs:
        print(f"- {game_id}/{file['name']}...", end="")
        if file['type'] == "dir":
            if not os.path.isdir(f"{path_to_games_dir}/{game_id}/{file['name']}"):
                os.mkdir(f"{path_to_games_dir}/{game_id}/{file['name']}")
            files_update("games", f"{game_id}/{file['name']}", file['files'])
            continue
        file_names.append(file['name'])
        file_hash = file_hash_(f"{path_to_games_dir}/{game_id}/{file['name']}")
        if not file_hash == "404":
            if file_hash == file["hash"]:
                print("OK", file_hash)
            else:
                print("FAIL")
                file['local_hash'] = file_hash
                error_files.append(file)
        else:
            print("404")
            error_files.append(file)

    print("---------------------------")
    for file in error_files:
        print(f"- {file['name']}...", end="")
        try:
            with open(f"{path_to_games_dir}/{game_id}/{file['name']}", "wb") as f:
                f.write(requests.get(file['url']).content)
            print("DONE!")
        except:
            print("FAIL!")
    print("=============================")