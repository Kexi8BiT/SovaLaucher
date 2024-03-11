import flet as ft
import json
from sound_effect import BoopSound
from ui import interface_button, interface_switch
from internets import get_updates
import time
class GamesPage:
    def __init__(self, id, web = False, config_start: {} = None, page: ft.Page = None, content_page = None):
        self.content_page = content_page
        self.id = id
        self.web = web
        self.config_start = config_start
        self.path = f"assets/games/{self.id}"
        with open(f"{self.path}/description.txt", "r", encoding='utf-8') as f:
            self.description = f.read()
        self.boop = BoopSound(page)
        self.page = page
        self.icon = ft.Image(f"{self.path}/icon.png")
        self.config = json.load(open(f"{self.path}/config.json", "r", encoding='utf-8'))
        news = ft.Column([], scroll=ft.ScrollMode.HIDDEN, expand=True)
        nes_col = get_updates(game_id=self.id)
        for new in nes_col:
            content_new = ft.Container(
                ft.Column([
                    ft.Row([ft.Text(f"{new['name']}", weight=ft.FontWeight.W_900, size=20)], spacing=15),
                    ft.Row([ft.Container(ft.Text(f"v{new['version']}", size=11, color=ft.colors.WHITE24),
                                         padding=ft.padding.only(top=1, bottom=1, left=5, right=5),
                                         bgcolor=ft.colors.WHITE12, border_radius=5),
                            ft.Text(f"{new['date']}", size=11, color=ft.colors.WHITE24)], spacing=5),
                    ft.Container(height=8),
                    ft.Markdown(f"{new['text']}")
                ], spacing=1),
                padding=5
            )
            news.controls.append(content_new)

        tags = ft.Row([
        ], wrap=True, spacing=3, width=280, alignment=ft.MainAxisAlignment.CENTER, expand=True)
        pop_tags = ["Популярно", "Лецензия", "3D"]
        for tag in self.config["tags"]:
            c = ft.Container(ft.Text(tag, size=12, color=ft.colors.WHITE60),
                         padding=ft.padding.only(top=2, bottom=2, left=8, right=8), bgcolor=ft.colors.WHITE10 if not tag in pop_tags else ft.colors.RED_400,
                         border_radius=5)
            tags.controls.append(c)


        self.content = ft.Container(ft.Row([
        ft.Container(ft.Column([

            ft.Container(
                ft.Column([
                    ft.Text("Описание", weight=ft.FontWeight.W_600, color=ft.colors.WHITE24),
                    ft.Container(ft.Text(self.description, selectable=True, size=15))
                ]),
                padding=10,
                height=200, width=500, bgcolor=ft.colors.BLACK26, border_radius=15, margin=ft.margin.only(top=10)),

            ft.Container(
                ft.Column([
                    ft.Text("Новости", weight=ft.FontWeight.W_600, color=ft.colors.WHITE24),
                    ft.Container(
                        news,
                        width=480, height=365)
                ]),
                padding=10,
                height=420, width=500, bgcolor=ft.colors.BLACK26, border_radius=15),
        ], scroll=ft.ScrollMode.ALWAYS), height=page.height),

        ft.Container(ft.Column([
            ft.Container(ft.Column([
                ft.Container(image_src=f"{self.path}/icon.png", height=150, width=150,
                             image_fit=ft.ImageFit.COVER, margin=ft.margin.only(top=20), border_radius=10),
                ft.Container(ft.Text(self.config["name"], size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)),
                tags,
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),width=280, height=550),
            ft.Container(ft.ElevatedButton("Играть", **interface_button), width=280, margin=ft.margin.only(bottom=10))
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.SPACE_BETWEEN), height=630, width=300, bgcolor=ft.colors.BLACK26, border_radius=15, margin=ft.margin.only(top=10))
        ], vertical_alignment=ft.CrossAxisAlignment.START), opacity=0, animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),)
    def set_page(self, e):
        self.content_page.content = self.content
        self.content_page.update()
        time.sleep(0.3)
        self.content.opacity=1
        self.content.update()