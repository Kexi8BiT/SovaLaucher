import flet as ft
from sound_effect import BoopSound
from ui import interface_button, interface_switch, interface_input
from internets import check_api

def go_to_settings(content, page: ft.Page):
    boop = BoopSound(page)
    boop.play()
    content.content = get_settings_page(page)
    content.update()
def get_settings_page(page: ft.Page):
    cdn = page.client_storage.get("cdn_url")
    if cdn == None:
        page.client_storage.set("cdn_url", "http://127.0.0.1:8000")
        print("CDN - УСТАНОВЛЕННО")
    def edit_cdn(e):
        def close(e):
            dialog.open = False
            page.update()

        def edit(e):
            edited_cdn = dialog.content.content.controls[0].value
            e.control.content = ft.ProgressRing(width=20, height=20, color=ft.colors.RED_400, bgcolor=ft.colors.BLACK26)
            e.control.update()
            if check_api(edited_cdn):
                close(e)
                page.client_storage.set("cdn_url", "http://127.0.0.1:8000")
            else:
                e.control.content = ft.Text("Сохранить")
                e.control.update()
                dialog.content.content.controls[0].error_text = "Некорректная ссылка"
                dialog.content.content.controls[0].update()

        def one_change(e):
            e.control.error_text = None
            dialog.content.content.controls[0].update()

        boop.play()
        cdn_url = page.client_storage.get("cdn_url")
        dialog = ft.AlertDialog(
            modal=True,
            shape=ft.ContinuousRectangleBorder(radius=50),
            content_padding=15,
            actions_padding=15,
            content=ft.Container(
                ft.Column([
                    ft.TextField(label="CDN", value=cdn_url, on_change=one_change, **interface_input),
                ]),
                height=60,
                width=300,

            ),
            actions=[ft.ElevatedButton("Сохранить", on_click=edit, **interface_button, width=150), ft.ElevatedButton("Отмена", on_click=close, **interface_button, width=150)]
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
    boop = BoopSound(page)
    settings = ft.Container(
        ft.Column([
            ft.Row([
                ft.ElevatedButton("Поменять путь установки", **interface_button,
                                  icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE_ROUNDED, on_click=boop.play_e),
                ft.ElevatedButton("Управление установками", **interface_button, icon=ft.icons.MEMORY,
                                  on_click=boop.play_e),
                ft.ElevatedButton("Отчистить кэш", **interface_button, icon=ft.icons.CLEAR, on_click=boop.play_e)]),
            ft.Row([
                ft.Container(content=ft.Row(
                    [ft.Icon(ft.icons.DO_NOT_DISTURB, color="white", size=20), ft.Text("Не беспокоить"),
                     ft.Switch(**interface_switch, on_change=boop.play_e)]), bgcolor="#1c2024", padding=10,
                             border_radius=10),
                ft.Container(content=ft.Row(
                    [ft.Icon(ft.icons.AUDIOTRACK_SHARP, color="white", size=20), ft.Text("Звуки"),
                     ft.Switch(**interface_switch, value=True, on_change=boop.play_e)]), bgcolor="#1c2024", padding=10,
                    border_radius=10),
            ]),
            ft.Row([
                ft.Container(content=ft.Row(
                    [ft.Icon(ft.icons.EXPLORE, color="white", size=20), ft.Text("Публичная сеть"),
                     ft.Switch(**interface_switch, on_change=boop.play_e)]), bgcolor="#1c2024", padding=10,
                    border_radius=10),
                ft.ElevatedButton("Изменить CDN", **interface_button, icon=ft.icons.CLOUD, on_click=edit_cdn)

            ])
        ]),
        height=page.window_height - 30
    )
    return settings