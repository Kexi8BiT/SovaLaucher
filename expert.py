import flet as ft
import string
import os
import psutil
from sound_effect import BoopSound
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


    def change_disk(disk):
        boop.play()
        catalog = disk
        page.client_storage.set("catalog_games", catalog)
        page.overlay.remove(message)
        page.update()
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
            bgcolor=ft.colors.with_opacity(0.5, ft.colors.BLACK), alignment=ft.alignment.center)

         ],

    )
    page.overlay.append(message)

    page.update()


