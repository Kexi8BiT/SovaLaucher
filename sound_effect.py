import flet as ft


class BoopSound:
    def __init__(self, page: ft.Page):
        self.boop = ft.Audio("assets/audio/boop.mp3", autoplay=False, volume=0.2)
        self.page = page
        page.overlay.append(self.boop)
        page.update()

    def play(self):
        is_sound = self.page.client_storage.get("on_sound")
        if is_sound != False:
            self.boop.play()

    def play_e(self, e):
        self.play()