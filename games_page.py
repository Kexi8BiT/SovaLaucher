import flet as ft
import json
from sound_effect import BoopSound
from game_run_page import GamesPage
import time
class Game_object(ft.UserControl):
    id: str = None
    web_content: bool = True

    def __init__(self, id: str, web_content: bool = False, page: ft.Page = None, content=None):
        super().__init__()
        self.id = id
        self.web_content = web_content
        self.path = f"assets/games/{self.id}"
        self.boop = BoopSound(page)
        self.play_button = ft.Container(
            ft.Icon(ft.icons.PLAY_ARROW_ROUNDED, size=40, color="white"),
            top=60, left=25, animate_offset=ft.animation.Animation(
                300, ft.AnimationCurve.EASE_OUT
            ),
            animate_opacity=ft.animation.Animation(
                300, ft.AnimationCurve.EASE_OUT
            ),
            offset=ft.Offset(1, 0),
            opacity=1,
            on_click=self.go_to_page_run

        )
        self.GAME_PAGE = GamesPage(id, web_content, None, page, content_page=content)

    def on_object_hover(self, e):
        e.control.content.shadow.blur_radius = 10 if e.data == "true" else 50
        e.control.update()

    def go_to_page(self, e):
        print(f"Открывается страница с описанием {self.id}")
        self.boop.play()
        self.content_container.height = 400
        self.content_container.scale = 1.5
        self.content_container.opacity = 0
        self.content_container.update()
        time.sleep(0.2)
        self.GAME_PAGE.set_page("e")

    def go_to_page_run(self, e):
        print(f"Сразу открывается игра {self.id}")
        self.boop.play()

    def build(self):
        with open(f"{self.path}/description.txt", "r", encoding='utf-8') as f:
            description = f.read()

        config = json.load(open(f"{self.path}/config.json", "r", encoding='utf-8'))
        self.content_container = ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        image_src=f"{self.path}/icon.png",
                        height=80, width=80, border_radius=10,
                        image_fit=ft.ImageFit.COVER,
                        top=15, left=15
                    ),
                    ft.Container(
                        ft.Text(config["name"], size=30, weight=ft.FontWeight.BOLD, color="white"),
                        left=100,
                        top=25
                    ),
                    ft.Container(
                        ft.Text(description, selectable=True, size=12),
                        left=100,
                        top=70,
                        bgcolor='black',
                        height=70,
                        width=400,
                        opacity=0.7,
                        border_radius=10,
                        padding=5
                    )
                ]
            ),
            height=150,
            width=800,
            border_radius=20,
            image_src=f"{self.path}/bg.jpg",
            image_fit=ft.ImageFit.FIT_WIDTH,
            on_click=self.go_to_page,
            # on_hover=self.on_object_hover,
            offset=ft.Offset(0, 0),
            animate_opacity=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            animate_offset=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
            animate=ft.Animation(100, ft.AnimationCurve.EASE_IN_OUT),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=50,
                color=config["color"],
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.NORMAL,

            )

        )

        object = ft.Container(
            self.content_container,
            on_hover=self.on_object_hover

        )

        return object

def go_to_main(content, page):
    boop = BoopSound(page)
    boop.play()
    content.content = get_games_page(page, content)
    content.update()



def get_games_page(page, content):
    games = ft.Container(
            ft.Column(
                [
                    ft.Container(
                      ft.Column([
                          ft.Text("Игры", size=30, weight=ft.FontWeight.BOLD, color="white"),
                          ft.Container(width=800, height=1, bgcolor="#5c5e60"),
                      ])
                    ),
                    Game_object(id="sovacraft", web_content=False, page=page, content=content),
                    Game_object(id="sovadash", web_content=False, page=page, content=content),
                    Game_object(id="sovadastry", web_content=False, page=page, content=content),

                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
                scroll=ft.ScrollMode.ALWAYS
            ),
            height=page.window_height,
        )
    return games