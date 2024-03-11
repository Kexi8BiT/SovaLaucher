import flet as ft

interface_button = {
        "color": ft.colors.WHITE,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor=ft.colors.WHITE24, overlay_color=ft.colors.with_opacity(0.5, ft.colors.RED_500), padding=20),
        "icon_color": "white",

    }
interface_switch = {
    "active_color" : ft.colors.WHITE,
    "active_track_color" : ft.colors.RED_400,
    "inactive_track_color" : "#1e1f22",
    "thumb_color" : ft.colors.WHITE,
    "inactive_thumb_color" : "white",
    "focus_color" : ft.colors.WHITE
}

interface_input = {

}