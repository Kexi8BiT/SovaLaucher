import flet as ft


class Toast():
    def __init__(self, page: ft.Page):
        self.page = page


    def loading(self) -> None:
        return

def main(page: ft.Page):
    toast = Toast(page)
    toast.loading()
    page.overlay.append(ft.Stack([ft.Container(ft.Row([ft.Container(ft.Row([ft.ProgressRing(height=10, width=10), ft.Text("Loading. qweqw dqwd qwd ..")]), height=50), ft.VerticalDivider(), ft.Icon(ft.icons.CHECK)]), bgcolor="black", padding=10, border_radius=10, border=ft.border.all(1, "#333333"), margin=10)]))
    page.update()


ft.app(target=main)