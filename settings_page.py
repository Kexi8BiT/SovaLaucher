import flet as ft
from sound_effect import BoopSound
from ui import interface_button, interface_switch, interface_input
from internets import check_api
from expert import disk_select, installed_games

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
    def on_off_sound(e):
        page.client_storage.set("on_sound", e.control.value)
        print("Звуки отключены" if e.control.value == False else "Звуки включены")
        boop.play()

    def on_dnd_change(e):
        page.client_storage.set("dnd", e.control.value)
        print("Не беспокоить выключен" if e.control.value == False else "Не беспокоить включен")
        if e.control.value == True:
            sound_switch.disabled = True
            sound_switch.value = False
            sound_switch.update()
            page.client_storage.set("on_sound", False)
        else:
            sound_switch.disabled = True
            sound_switch.value = True
            sound_switch.update()
            page.client_storage.set("on_sound", True)
        boop.play()

    on_sound = page.client_storage.get("on_sound")
    if on_sound == None:
        page.client_storage.set("on_sound", True)

    dnd = page.client_storage.get("dnd")
    if dnd == None:
        page.client_storage.set("dnd", False)

    def open_installers(e):
        boop.play()
        installed_games(page)

    sound_switch = ft.Switch(**interface_switch, value=page.client_storage.get("on_sound"), on_change=on_off_sound, disabled=True if page.client_storage.get("dnd") == True else False)
    settings = ft.Container(
        ft.Column([
            ft.Row([
                ft.ElevatedButton("Поменять диск установки", **interface_button,
                                  icon=ft.icons.DRIVE_FILE_RENAME_OUTLINE_ROUNDED, on_click=lambda _: disk_select(page)),
                ft.ElevatedButton("Управление установками", **interface_button, icon=ft.icons.MEMORY,
                                  on_click=open_installers),
                ft.ElevatedButton("Отчистить кэш", **interface_button, icon=ft.icons.CLEAR, on_click=boop.play_e)]),
            ft.Row([
                ft.Container(content=ft.Row(
                    [ft.Icon(ft.icons.DO_NOT_DISTURB, color="white", size=20), ft.Text("Не беспокоить"),
                     ft.Switch(**interface_switch, on_change=on_dnd_change, value=page.client_storage.get("dnd"))]), bgcolor="#1c2024", padding=10,
                             border_radius=10),
                ft.Container(content=ft.Row(
                    [ft.Icon(ft.icons.AUDIOTRACK_SHARP, color="white", size=20), ft.Text("Звуки"),
                     sound_switch]), bgcolor="#1c2024", padding=10,
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