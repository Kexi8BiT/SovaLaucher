import flet as ft

interface_button = {
        "color": ft.colors.WHITE,
        "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), bgcolor=ft.colors.WHITE24, overlay_color=ft.colors.with_opacity(0.05, ft.colors.WHITE), padding=20),
        "icon_color": "white",

    }
interface_switch = {
    "active_color": ft.colors.WHITE,
    "active_track_color": ft.colors.RED_400,
    "inactive_track_color": "#1e1f22",
    "thumb_color": ft.colors.WHITE,
    "inactive_thumb_color" : "white",
    "focus_color" : ft.colors.WHITE
}

navigation_button = {
    "width": 250,
    "height": 45,
    "bgcolor": ft.colors.TRANSPARENT,
    "color": ft.colors.WHITE,
    "icon_color": ft.colors.WHITE,
    "style": ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), bgcolor=ft.colors.TRANSPARENT,
                            surface_tint_color=ft.colors.TRANSPARENT, shadow_color=ft.colors.TRANSPARENT, overlay_color=ft.colors.with_opacity(0.1, ft.colors.WHITE)),
}

interface_input = {
    "color": "#FFFFFF",
    "cursor_color": "#FFFFFF",
    "border_color": ft.colors.WHITE,
    "border_radius": 15,
    "focused_border_color": ft.colors.RED_400
}