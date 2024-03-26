import flet as ft
from ui import interface_button
import requests
from internets import get_updates
md1 = """
# Добро пожаловать в SovaLauncher!


SovaLauncher - фанатская переделка оригинального SovaLaucher, в отличии от оригинала этот лаунчер имеет множество забавных фич и дополнений




|**SovaLauncher (Этот)**                |**SovaLaucher (Оффициальный)**       |
|---------------------------------------|-------------------------------------|
|Красивый интерфейс ✅                  |Красивый интерфейс ❌               |
|Открытый исходный код ✅               |Открытый исходный код ❌            |
|Поддержка всех игр ✅                  |Поддержка всех игр ✅               |
|Поддержка плагинов ❌                  |Поддержка плагинов ❌               | 
|Быстрое обновление ✅                  |Быстрое обновление ❌              |
"""
md2 = """

"""
def get_main_page_home(page: ft.Page):
    base_url = page.client_storage.get("cdn_url")
    def open_devs(e):
        req = requests.get(base_url + "/info/devloper")
        if req.status_code == 200:
            req = req.json()
            dev = req["devloper"]
            dialog = ft.AlertDialog(
                modal=False,
                title=ft.Text("Разработчики"),
                content=ft.Container(
                    ft.Column(
                        [
                            ft.Container(ft.Column([ft.Image(src=dev["icon"], height=100, border_radius=50),
                                                    ft.Text(dev["name"], size=30, weight=ft.FontWeight.BOLD,
                                                            color=ft.colors.BLUE_400)],
                                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                         on_click=lambda e: page.launch_url(dev["link"])),
                            ft.Container(ft.Text(dev['description'], selectable=True), padding=10,
                                         bgcolor=ft.colors.BLACK12, border_radius=20)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    height=300,
                    width=200
                )
            )
            page.dialog = dialog
            dialog.open = True
            page.update()

        else:
            page.error(req.status_code)

    def update_history(e):
        news = ft.Column([], scroll=ft.ScrollMode.HIDDEN, expand=True)
        nes_col = get_updates(game_id="sovalauncher")
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

        dialog = ft.AlertDialog(
            modal=False,
            title=ft.Text("Обновления"),
            content=ft.Container(news, width=500, height=400)
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def supp(e):
        dialog = ft.AlertDialog(
            modal=False,
            title=ft.Text("Просто напишите мне в лс и скажите какой я крутой"))
        page.dialog = dialog
        dialog.open = True
        page.update()

    content = ft.Container(
        ft.Column(
            [
                ft.Markdown(
                    md1,
                    selectable=True,
                    extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                    on_tap_link=lambda e: page.launch_url(e.data),
                ),
                ft.Row([ft.Text("Да, лаунчер имеет открытый исходный код, репозиторий лежит на "), ft.ElevatedButton(content=ft.Row([ft.Image(src="assets/icons/gitdark.png", height=20), ft.Text("GitHub")]), **interface_button, on_click=lambda e: page.launch_url("https://github.com/Kexi8BiT/SovaLaucher"))], spacing=5),
                ft.Container(ft.Row([ft.ElevatedButton("Разработчики", **interface_button, icon=ft.icons.PEOPLE, on_click=open_devs),
                                     ft.ElevatedButton("История обновлений", **interface_button, icon=ft.icons.UPDATE, on_click=update_history),
                                     ft.ElevatedButton("Поддержка", **interface_button, icon=ft.icons.HEART_BROKEN, on_click=supp),

                                     ]))
            ]
        ),
        height=page.height,
        width=700
    )

    return content
