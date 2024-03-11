import flet as ft
from navifation import get_elements
import json
from internets import get_ip, get_updates
from sound_effect import BoopSound
import ctypes
from BlurWindow.blurWindow import GlobalBlur
from games_page import go_to_main, get_games_page
from settings_page import go_to_settings, get_settings_page
from ui import interface_button, interface_switch
from game_run_page import GamesPage
class Blur:
    @staticmethod
    def get_current_hwnd():
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        GlobalBlur(hwnd)
sound = True

launcher_name = "SovaLauncher"



def main(page: ft.Page):


    page.window_title_bar_hidden = True

    page.title = launcher_name
    height = 700
    width = 1100
    page.window_resizable = False
    page.window_height = height
    page.window_width = width
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK
    page.spacing = 0
    boop = BoopSound(page)
    page.overlay.append(ft.Audio("assets/audio/start.mp3", autoplay=True, volume=0.2))
    content = ft.Container()
    GAMES = ft.Container(get_games_page(page, content))
    SETTINGS = ft.Container(get_settings_page(page))
    content.content = SETTINGS






    drag_area, nav_left = get_elements(page, height, lambda _: go_to_main(content, page), lambda _: go_to_settings(content, page))

    page.add(drag_area)
    page.add(ft.Row([nav_left, content]))


ft.app(main)
