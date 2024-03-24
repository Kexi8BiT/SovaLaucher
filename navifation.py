import flet as ft
from sound_effect import BoopSound

launcher_name = "PixelLauncher"




navigation_button = {
    "width": 250,
    "height": 45,
    "bgcolor": ft.colors.TRANSPARENT,
    "color": ft.colors.WHITE,
    "icon_color": ft.colors.WHITE,
    "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), bgcolor=ft.colors.TRANSPARENT,
                            surface_tint_color=ft.colors.TRANSPARENT, shadow_color=ft.colors.TRANSPARENT, overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE)),
}

def get_elements(page, height, main, settings):
    def close(e):
        page.window_minimized = True
        page.update()

    navigation = ft.Container(ft.Column([ft.Container(
        ft.Image("assets/logo.png", width=150),
        margin=ft.margin.only(bottom=40, top=20), on_click=lambda _: page.launch_url("https://www.sovagroup.one"), tooltip="site:https://www.sovagroup.one"),
                                         ft.ElevatedButton("Главная", **navigation_button, on_click=main),
                                         ft.ElevatedButton("Библиотека", **navigation_button, on_click=lambda _: BoopSound(page).play()),
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