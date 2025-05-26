import flet as ft


def main(page: ft.Page):
    page.title = "File Compare Tool"

    file1_display = ft.TextField(label="Первый файл", read_only=True)
    file2_display = ft.TextField(label="Второй файл", read_only=True)

    page.add(
        file1_display,
        file2_display
    )
ft.app(main)
