import flet as ft

def main(page: ft.Page):
    page.title = "Magno Efren - Flet Projects Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.SURFACE_VARIANT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.spacing = 20

    # Header: Download Keyview
    download_row = ft.Row(
        [
            ft.Text("📥 Descargar Keyview", size=20, weight=ft.FontWeight.BOLD),
            ft.TextButton(
                "Descargar Keyview",
                icon=ft.icons.DOWNLOAD,
                style=ft.ButtonStyle(bgcolor=ft.colors.BLUE),
                on_click=lambda _: page.launch_url("https://drive.usercontent.google.com/download?id=1_kZ5VOEfAjmVLrRLKnodgEb11I0zwtzB&export=download&authuser=0"),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # YouTube Channel
    youtube_row = ft.Row(
        [
            ft.Text("Interfaces Gráficas en Python con Flet", size=18, weight=ft.FontWeight.BOLD),
            ft.IconButton(
                icon=ft.icons.YOUTUBE,
                icon_color=ft.colors.RED,
                icon_size=32,
                on_click=lambda _: page.launch_url("https://www.youtube.com/c/MagnoEfren"),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Project 1: Form, CRUD
    crud_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Form, CRUD, export data in Excel and PDF", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Tutorial demonstrates creating a Python CRUD system with Flet and SQLite.\n"
                        "Efficient data management via responsive form (name, age, email, phone).\n"
                        "Includes CRUD operations and data export to PDF/Excel.\n"
                        "Enhances application capabilities for streamlined data handling.",
                        size=14,
                    ),
                    ft.ElevatedButton(
                        "Ver en YouTube",
                        icon=ft.icons.PLAY_ARROW,
                        on_click=lambda _: page.launch_url("https://youtu.be/AAxijGx9_Pc"),
                    ),
                    ft.Image(
                        src="https://github.com/MagnoEfren/apps_in_flet/blob/main/Form_CRUD/ss.webp",
                        width=300,
                        height=200,
                        fit=ft.ImageFit.COVER,
                        border_radius=10,
                    ),
                ],
                spacing=10,
            ),
            padding=20,
        ),
    )

    # Project 2: Portfolio Web Responsive
    portfolio_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Portafolio Web Responsive con Flet", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Aprende a crear un portafolio web responsive con Python y Flet.\n"
                        "Incluye modos oscuro y claro para mejorar la experiencia del usuario.\n"
                        "Optimizado para cualquier dispositivo, ideal para mostrar tus proyectos y habilidades.\n"
                        "Fácil de personalizar y adaptarse a tu estilo.",
                        size=14,
                    ),
                    ft.ElevatedButton(
                        "Ver en YouTube",
                        icon=ft.icons.PLAY_ARROW,
                        on_click=lambda _: page.launch_url("https://youtu.be/AAxijGx9_Pc"),
                    ),
                    ft.Image(
                        src="https://github.com/MagnoEfren/flet/blob/main/PortfolioWeb/222.png",
                        width=300,
                        height=200,
                        fit=ft.ImageFit.COVER,
                        border_radius=10,
                    ),
                ],
                spacing=10,
            ),
            padding=20,
        ),
    )

    # Project 3: Publish App to Android
    android_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Publish an app on Flet to Android", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Commands:\n"
                        "flet create <myapp> - Creates a folder with assets and main files.\n"
                        "flet build apk - Creates a build folder with the .apk file.\n\n"
                        "Steps:\n"
                        "- Install the Android SDK\n"
                        "- Install the Flutter SDK 3.16 or above\n"
                        "- Install the Java JDK\n"
                        "- Verify Java version matches Gradle compatibility.\n\n"
                        "Watch the video on YouTube here 👇📱",
                        size=14,
                    ),
                    ft.ElevatedButton(
                        "Ver en YouTube",
                        icon=ft.icons.PLAY_ARROW,
                        on_click=lambda _: page.launch_url("https://youtu.be/rnot_xtKTLI"),
                    ),
                    ft.Image(
                        src="https://github.com/MagnoEfren/flet/blob/main/App%20Flet%20to%20APK/fletcal/assets/flet-to-apk.png",
                        width=300,
                        height=200,
                        fit=ft.ImageFit.COVER,
                        border_radius=10,
                    ),
                ],
                spacing=10,
            ),
            padding=20,
        ),
    )

    # Support Section
    support_row = ft.Row(
        [
            ft.Text("Si desea apoyar puede hacerlo aquí:", size=14, italic=True),
            ft.Text("Nunca es obligatorio, pero se agradece mucho. 😊", size=14, italic=True),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    support_buttons = ft.Row(
        [
            ft.ElevatedButton(
                "PayPal",
                icon=ft.icons.PAYMENT,
                style=ft.ButtonStyle(bgcolor=ft.colors.AMBER),
                on_click=lambda _: page.launch_url("https://www.paypal.com/paypalme/magnoefren"),
            ),
            ft.ElevatedButton(
                "Unirse a YouTube",
                icon=ft.icons.SUBSCRIPTIONS,
                style=ft.ButtonStyle(bgcolor=ft.colors.BLUE),
                on_click=lambda _: page.launch_url("https://www.youtube.com/channel/UCBwN7Z5LWQAJ_6ueSEzDtGQ/join"),
            ),
            ft.ElevatedButton(
                "Patreon",
                icon=ft.icons.HEART_BROKEN,
                style=ft.ButtonStyle(bgcolor=ft.colors.PINK),
                on_click=lambda _: page.launch_url("https://www.patreon.com/magnoefren"),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        wrap=True,
    )

    # Playlist
    playlist_row = ft.Row(
        [
            ft.Text("Mis Videos de YouTube", size=18, weight=ft.FontWeight.BOLD),
            ft.IconButton(
                icon=ft.icons.PLAYLIST_PLAY,
                icon_size=24,
                on_click=lambda _: page.launch_url("https://www.youtube.com/playlist?list=PLfSVB4Wge3DLFBx_RMcCCkeGWhOuDeB3-"),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Main Column
    content = ft.Column(
        [
            download_row,
            ft.Divider(),
            youtube_row,
            ft.Divider(),
            crud_card,
            ft.Divider(),
            portfolio_card,
            ft.Divider(),
            android_card,
            ft.Divider(),
            support_row,
            support_buttons,
            ft.Divider(),
            playlist_row,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(
        ft.Container(
            content=content,
            padding=20,
            expand=True,
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
