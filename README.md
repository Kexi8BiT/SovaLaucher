## Что-ж этим проектом я хотел помочь Сг стать более современнее, но к сожалению заморожен, возможно на всегда

Это простой интерфейс лаунчера, без функцианала, можно добавлять свои игры и приложения

# Начало
# !!! Работает на Python 3.12 !!!
Для начала установите все зависимости
```commandline
pip install -r requirements.txt
```

После этого вы можете запустить приложение через
```commandline
flet run
```
Или 
```commandline
python main.py
```

# Структура
Структура максимально простая
```text
- asstes *тут хранятся файлы с которыми работает лаунчер
|- audio * тут аудио файлы
    |- boop.mp3 (звук нажатия)
    |- message.mp3 (неиспользуемый звук оповещения)
    |- start.mp3 (проигрывается при старте лаунчера)
|- games *тут игры и их описание
    |- sovadash
        |- bg.jpg
        |- config.json
        |- description.txt
        |- icon.png
    |- ...
```
впринципе все что нужно знать.
Настроить дополнительные вкладки можно в games_page.py

все интернет запросы и данные прописаны в internets.py
llamareq.py - лол я сам хз что это

также для настройки интерфейса используется ui.py в нем прописаны ввсе стили кнопок и слайдеров в лаунчере

client_storage:
```python
on_sound: bool # Настройка - обозначает проигрывается ли звуки в лаунчере
dnd: bool # Не беспокоить
catalog_games: str # Каталог (Диск) на котором хранятся игры
cdn_url: str # Базовый апи с которым работает лаунчер
```



дальше ебитесь сами, мой лс всегда открыт а также есть issues или как там их