import flet as ft
import socket
import threading
import json


def show_notifical(title, message):
    def main(page: ft.Page):
        page.title = title
        page.window_title_bar_hidden = True
        page.window_resizable = False
        page.window_width = 400
        page.window_height = 200
        page.padding = 0
        page.theme_mode = ft.ThemeMode.DARK
        page.spacing = 0
        page.add(ft.Row(
            [
                ft.WindowDragArea(ft.Container(ft.Row([ft.Text(title, weight=ft.FontWeight.BOLD), ft.Container(height=16, width=16, bgcolor=ft.colors.RED_400, border_radius=8, on_click=lambda _: page.window_destroy())], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), bgcolor=ft.colors.BLACK26, padding=5), expand=True)
            ]
        ))
        page.add(ft.Container(ft.Text(message, size=15, selectable=True, weight=ft.FontWeight.NORMAL), margin=10))

    ft.app(main)




def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            json_message = json.loads(message)
            show_notifical(json_message['title'], json_message['text'])
        except:
            print('Error occurred!')
            client.close()
            break

host = 'localhost'
port = 6084

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

receive_thread = threading.Thread(target=receive)
receive_thread.start()