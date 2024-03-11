import flet as ft
from sound_effect import BoopSound
from ui import interface_button, interface_switch, interface_input


def go_to_settings(content, page):
    boop = BoopSound(page)
    boop.play()
    content.content = get_settings_page(page)
    content.update()
def get_settings_page(page: ft.Page):
    def edit_cdn(e):
        def close(e):
            dialog.open = False
            page.update()
        boop.play()
        dialog = ft.AlertDialog(
            modal=True,
            shape=ft.ContinuousRectangleBorder(radius=20),
            content=ft.Container(
                ft.Column([
                    ft.TextField(label="CDN", value="https://cdn.sovagroup.one", on_change=boop.play_e, color="#FFFFFF", cursor_color="#FFFFFF", border_color=ft.colors.WHITE, border_radius=15, focused_border_color=ft.colors.RED_400),
                ]),
                height=50,
                width=300
            ),
            actions=[ft.ElevatedButton("Сохранить", on_click=boop.play_e, **interface_button, width=150), ft.ElevatedButton("Отмена", on_click=close, **interface_button, width=150)]
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