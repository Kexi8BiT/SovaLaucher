import flet as ft
import string
import os
import psutil
from sound_effect import BoopSound
import json
from ui import interface_button

def get_available_drives():
    return [drive for drive in string.ascii_uppercase if os.path.exists(drive + ':\\')]

def get_disk_usage(drive_letter):
    disk_usage = psutil.disk_usage(drive_letter + ':\\')
    percent_used = disk_usage.percent / 100
    gb_free = disk_usage.free / (2**30)  # конвертируем байты в гигабайты
    return percent_used, gb_free


def disk_select(page: ft.Page):
    boop = BoopSound(page)
    boop.play()
    catalog = page.client_storage.get("catalog_games")
    if catalog is None:
        catalog = "C"
        page.client_storage.set("catalog_games", catalog)

    def close(e):
        page.overlay.remove(message)
        page.update()

    def on_bg_click(e):
        print("on_bg_click")
    def change_disk(disk):
        boop.play()
        catalog = disk
        page.client_storage.set("catalog_games", catalog)
        close(disk)

    def prew_change_disk(e):
        boop.play()
        disk = e.control.value
        percent_used, gb_free = get_disk_usage(disk)
        progress.value = percent_used
        progress.update()
        progress_right.value = f"{gb_free:.2f} GB"
        progress_right.update()
        if gb_free < 1:
            btn.disabled = True
            btn.update()
        else:
            btn.disabled = False
            btn.update()

    catalogs = get_available_drives()
    dd = ft.Dropdown(width=380, value=page.client_storage.get("catalog_games"),
                options=[ft.dropdown.Option(catalog) for catalog in catalogs],
                border_color=ft.colors.with_opacity(0.1, ft.colors.BLACK), border_radius=30,
                prefix_icon=ft.icons.STORAGE_ROUNDED, on_change=prew_change_disk)

    percent_used, gb_free = get_disk_usage(page.client_storage.get("catalog_games"))
    progress = ft.ProgressBar(width=295, bgcolor=ft.colors.BLACK12, color=ft.colors.WHITE, value=percent_used)
    progress_right = ft.Text(f"{gb_free:.2f} GB")

    btn = ft.ElevatedButton("Применить", width=380, on_click=lambda _: change_disk(dd.value), disabled=True if gb_free <  1 else False, bgcolor=ft.colors.BLACK12, style=ft.ButtonStyle(bgcolor=ft.colors.TRANSPARENT, shadow_color=ft.colors.TRANSPARENT, overlay_color=ft.colors.TRANSPARENT, surface_tint_color=ft.colors.TRANSPARENT, ),color=ft.colors.WHITE)
    message = ft.Stack(
        [ft.Container(
            ft.Container(
                width=400,
                height=200,
                bgcolor="#2e2e2e",
                border_radius=20,
                border=ft.border.all(1, ft.colors.BLACK12),
                padding=20,
                content=ft.Column([
                    ft.Text("Выберите каталог", size=20, color=ft.colors.WHITE),
                    dd,
                    ft.Row([progress, progress_right]),
                    btn
                ])
        ),
            bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK), alignment=ft.alignment.center, blur=ft.Blur(10, 10))

         ],

    )
    page.overlay.append(message)

    page.update()


def installed_games(page: ft.Page):
    boop = BoopSound(page)
    def get_game_object(game_id):
        with open(f"assets/games/{game_id}/config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        object = ft.Container(
                            ft.Row(
                                [
                                    ft.Container(
                                        ft.Row(
                                            [
                                                ft.Image(height=50, width=50, src=f"assets/games/{game_id}/icon.png", border_radius=10),
                                                ft.Container(ft.Column([ft.Text(config["name"], weight=ft.FontWeight.BOLD), ft.Text("214 MB", color="#585858")], spacing=2))
                                            ]
                                        )
                                    ),
                                    ft.Container(ft.Row([ft.IconButton(icon=ft.icons.RESTART_ALT, icon_color=ft.colors.WHITE, style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, shape=ft.RoundedRectangleBorder(radius=15))), ft.IconButton(ft.icons.FOLDER, icon_color=ft.colors.WHITE, style=ft.ButtonStyle(bgcolor=ft.colors.AMBER_900, shape=ft.RoundedRectangleBorder(radius=15))), ft.IconButton(ft.icons.DELETE_FOREVER, icon_color=ft.colors.WHITE, style=ft.ButtonStyle(bgcolor=ft.colors.RED_700, shape=ft.RoundedRectangleBorder(radius=15)))]))

                                 ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            )
                        )
        return object

    files = os.listdir(f"assets/games")
    def close(e):
        boop.play()
        page.overlay.remove(content)
        page.update()
    content = ft.Stack([
            ft.Container(
                ft.Container(
                    ft.Column([
                        ft.Container(
                            ft.Column([
                                get_game_object(file) for file in files
                            ], spacing=50, scroll=ft.ScrollMode.HIDDEN),
                            height=400,
                            border_radius=20
                        ),
                        ft.Container(
                            ft.ElevatedButton("Назад", on_click=close, **interface_button, width=150),
                            alignment=ft.alignment.center
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    bgcolor="#1E1E1E",
                    height=500,
                    width=900,
                    border_radius=20,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=10,
                        color='black',
                        offset=ft.Offset(0, 10),
                        blur_style=ft.ShadowBlurStyle.NORMAL,

                    ),
                    padding=20
                ),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK),
                blur=ft.Blur(10, 10)
            )
        ])
    page.overlay.append(
        content
    )
    page.update()

