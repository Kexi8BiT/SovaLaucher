import flet as ft
from PIL import Image
import io
import base64
from ui import navigation_button
launcher_name = "PixelLauncher"


def colorize_image(rgb, image_path):
    image = Image.open(image_path).convert('RGB')
    colored_image = Image.new('RGB', image.size, rgb)
    colored_image = Image.blend(colored_image, image, 0.5)
    byte_stream = io.BytesIO()
    colored_image.save(byte_stream, format='PNG')
    byte_stream.seek(0)
    base64_image = base64.b64encode(byte_stream.getvalue()).decode('utf-8')
    return base64_image


logo_path = "assets/logo_.png"
rgb = (100, -5, -2)

def get_elements(page, height, main, settings, library):
    def close(e):
        page.window_minimized = True
        page.update()


    image_base64 = colorize_image(rgb, logo_path)
    navigation = ft.Container(ft.Column([ft.Container(
        ft.Image(src_base64=image_base64, width=150, border_radius=30),
        margin=ft.margin.only(bottom=40, top=20), on_click=lambda _: page.launch_url("https://www.sovagroup.one"), tooltip="site:https://www.sovagroup.one"),
                                         ft.ElevatedButton("Главная", **navigation_button, on_click=main),
                                         ft.ElevatedButton("Библиотека", **navigation_button, on_click=library),
                                         ft.ElevatedButton("Настройки", **navigation_button, on_click=settings),
                                         ft.Divider(),
                                         ft.ElevatedButton("Оффициальный лаунчер", **navigation_button, icon=ft.icons.OPEN_IN_NEW,  on_click=lambda _: page.launch_url("https://www.sovagroup.one/sovalaucher"), tooltip="sovagroup:official-launcher"),
                                        ], spacing=0,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER), bgcolor="#101010", width=250,
                              height=height)

    window_drag = ft.Row(
            [
                ft.WindowDragArea(
                    ft.Container(ft.Row([ft.Row([ft.Container(height=17, width=17, bgcolor=ft.colors.RED_400, border_radius=15,
                                                      on_click=lambda _: page.window_destroy()),
                                         ft.Container(height=17, width=17, bgcolor=ft.colors.AMBER_300, border_radius=15,
                                                      on_click=close)]), ft.Text(launcher_name, size=12, weight=ft.FontWeight.BOLD, color="#565656"), ft.Container()], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), bgcolor="#151515", padding=10), expand=True, maximizable=False)
            ]
        )

    return window_drag, navigation