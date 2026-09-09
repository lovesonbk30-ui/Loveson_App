import flet as ft


def main(page: ft.Page):
    page.title = "Loveson App"
    page.padding = 20

    page.add(
        ft.Text(
            "🎉 Flet is working!",
            size=30,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Text(
            "Android + Pydroid 3",
            size=18,
        ),
    )


if __name__ == "__main__":
    ft.run(main)