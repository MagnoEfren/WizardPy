import flet as ft

def main(page: ft.Page):
    page.title = "Magno Efren - Flet Projects Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f0f4f8"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    
    # Función para crear tarjetas con efecto glass
    def create_glass_card(content, gradient_colors=None):
        if gradient_colors is None:
            gradient_colors = ["#ffffff", "#f8f9fa"]
        
        return ft.Container(
            content=content,
            bgcolor="#ffffff",
            border_radius=20,
            padding=25,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=20,
                color=ft.Colors.with_opacity(0.1, "#000000"),
                offset=ft.Offset(0, 4),
            ),
            border=ft.border.all(1, ft.Colors.with_opacity(0.2, "#e0e0e0")),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    ft.Colors.with_opacity(0.95, gradient_colors[0]),
                    ft.Colors.with_opacity(0.85, gradient_colors[1]),
                ],
            ),
        )

    # Header principal con efecto glass
    header = create_glass_card(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=50, color="#667eea"),
                        ft.Column(
                            [
                                ft.Text(
                                    "Magno Efren",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    color="#2d3748",
                                ),
                                ft.Text(
                                    "Flet Projects Portfolio",
                                    size=16,
                                    color="#718096",
                                ),
                            ],
                            spacing=2,
                        ),
                    ],
                    spacing=15,
                ),
                ft.Divider(height=20, color=ft.Colors.with_opacity(0.1, "#000000")),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.DOWNLOAD, size=20, color="#ffffff"),
                                    ft.Text("Descargar Keyview", size=14, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ],
                                spacing=8,
                            ),
                            bgcolor="#667eea",
                            border_radius=12,
                            padding=ft.padding.symmetric(horizontal=20, vertical=12),
                            ink=True,
                            on_click=lambda _: page.launch_url("https://drive.usercontent.google.com/download?id=1_kZ5VOEfAjmVLrRLKnodgEb11I0zwtzB&export=download&authuser=0"),
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.YOUTUBE_SEARCHED_FOR, size=20, color="#ffffff"),
                                    ft.Text("Canal YouTube", size=14, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ],
                                spacing=8,
                            ),
                            bgcolor="#f56565",
                            border_radius=12,
                            padding=ft.padding.symmetric(horizontal=20, vertical=12),
                            ink=True,
                            on_click=lambda _: page.launch_url("https://www.youtube.com/c/MagnoEfren"),
                        ),
                    ],
                    wrap=True,
                    spacing=15,
                    run_spacing=10,
                ),
            ],
            spacing=20,
        ),
        ["#e3f2fd", "#bbdefb"],
    )

    # Tarjeta de proyecto 1: CRUD
    project1 = create_glass_card(
        ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src="https://github.com/MagnoEfren/apps_in_flet/blob/main/Form_CRUD/ss.webp?raw=true",
                        fit=ft.ImageFit.COVER,
                        border_radius=12,
                    ),
                    border_radius=12,
                    height=200,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                ),
                ft.Text(
                    "Form, CRUD & Export",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#2d3748",
                ),
                ft.Text(
                    "Sistema CRUD completo con Python, Flet y SQLite. Gestión eficiente de datos con formulario responsivo y exportación a PDF/Excel.",
                    size=13,
                    color="#718096",
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.PLAY_ARROW, size=18, color="#ffffff"),
                            ft.Text("Ver Tutorial", size=13, color="#ffffff", weight=ft.FontWeight.BOLD),
                        ],
                        spacing=5,
                    ),
                    bgcolor="#48bb78",
                    border_radius=10,
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                    ink=True,
                    on_click=lambda _: page.launch_url("https://youtu.be/AAxijGx9_Pc"),
                ),
            ],
            spacing=15,
        ),
        ["#f0fff4", "#c6f6d5"],
    )

    # Tarjeta de proyecto 2: Portfolio
    project2 = create_glass_card(
        ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src="https://github.com/MagnoEfren/flet/blob/main/PortfolioWeb/222.png?raw=true",
                        fit=ft.ImageFit.COVER,
                        border_radius=12,
                    ),
                    border_radius=12,
                    height=200,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                ),
                ft.Text(
                    "Portfolio Web Responsive",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#2d3748",
                ),
                ft.Text(
                    "Crea un portafolio web responsive con Python y Flet. Incluye modos oscuro y claro, optimizado para cualquier dispositivo.",
                    size=13,
                    color="#718096",
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.PLAY_ARROW, size=18, color="#ffffff"),
                            ft.Text("Ver Tutorial", size=13, color="#ffffff", weight=ft.FontWeight.BOLD),
                        ],
                        spacing=5,
                    ),
                    bgcolor="#667eea",
                    border_radius=10,
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                    ink=True,
                    on_click=lambda _: page.launch_url("https://youtu.be/AAxijGx9_Pc"),
                ),
            ],
            spacing=15,
        ),
        ["#faf5ff", "#e9d5ff"],
    )

    # Tarjeta de proyecto 3: Android
    project3 = create_glass_card(
        ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src="https://raw.githubusercontent.com/MagnoEfren/flet/refs/heads/main/App%20Flet%20to%20APK/fletcal/assets/flet-to-apk.png",
                        fit=ft.ImageFit.COVER,
                        border_radius=12,
                    ),
                    border_radius=12,
                    height=200,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                ),
                ft.Text(
                    "Publicar App en Android",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#2d3748",
                ),
                ft.Text(
                    "Aprende a crear y publicar aplicaciones Flet en Android. Incluye comandos, instalación de SDK y configuración completa.",
                    size=13,
                    color="#718096",
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Icon(ft.Icons.PLAY_ARROW, size=18, color="#ffffff"),
                            ft.Text("Ver Tutorial", size=13, color="#ffffff", weight=ft.FontWeight.BOLD),
                        ],
                        spacing=5,
                    ),
                    bgcolor="#ed8936",
                    border_radius=10,
                    padding=ft.padding.symmetric(horizontal=15, vertical=10),
                    ink=True,
                    on_click=lambda _: page.launch_url("https://youtu.be/rnot_xtKTLI"),
                ),
            ],
            spacing=15,
        ),
        ["#fffaf0", "#feebc8"],
    )

    # Grid responsivo de proyectos
    projects_grid = ft.ResponsiveRow(
        [
            ft.Container(content=project1, col={"sm": 12, "md": 6, "lg": 4}),
            ft.Container(content=project2, col={"sm": 12, "md": 6, "lg": 4}),
            ft.Container(content=project3, col={"sm": 12, "md": 6, "lg": 4}),
        ],
        spacing=20,
        run_spacing=20,
    )

    # Sección de apoyo
    support_section = create_glass_card(
        ft.Column(
            [
                ft.Text(
                    "💖 Apoya el Proyecto",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#2d3748",
                ),
                ft.Text(
                    "Nunca es obligatorio, pero se agradece mucho. Tu apoyo ayuda a crear más contenido de calidad.",
                    size=14,
                    color="#718096",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.PAYMENT, size=18, color="#ffffff"),
                                    ft.Text("PayPal", size=13, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ],
                                spacing=5,
                            ),
                            bgcolor="#fbbf24",
                            border_radius=10,
                            padding=ft.padding.symmetric(horizontal=20, vertical=12),
                            ink=True,
                            on_click=lambda _: page.launch_url("https://www.paypal.com/paypalme/magnoefren"),
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.SUBSCRIPTIONS, size=18, color="#ffffff"),
                                    ft.Text("YouTube", size=13, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ],
                                spacing=5,
                            ),
                            bgcolor="#3b82f6",
                            border_radius=10,
                            padding=ft.padding.symmetric(horizontal=20, vertical=12),
                            ink=True,
                            on_click=lambda _: page.launch_url("https://www.youtube.com/channel/UCBwN7Z5LWQAJ_6ueSEzDtGQ/join"),
                        ),
                        ft.Container(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.Icons.FAVORITE, size=18, color="#ffffff"),
                                    ft.Text("Patreon", size=13, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ],
                                spacing=5,
                            ),
                            bgcolor="#ec4899",
                            border_radius=10,
                            padding=ft.padding.symmetric(horizontal=20, vertical=12),
                            ink=True,
                            on_click=lambda _: page.launch_url("https://www.patreon.com/magnoefren"),
                        ),
                    ],
                    wrap=True,
                    spacing=15,
                    run_spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ["#fff5f5", "#fed7d7"],
    )

    # Sección de playlist
    playlist_section = create_glass_card(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "📺 Mis Videos de YouTube",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="#2d3748",
                        ),
                        ft.Text(
                            "Explora toda la playlist completa",
                            size=13,
                            color="#718096",
                        ),
                    ],
                    expand=True,
                ),
                ft.Container(
                    content=ft.Icon(ft.Icons.PLAYLIST_PLAY, size=28, color="#ffffff"),
                    bgcolor="#667eea",
                    border_radius=12,
                    padding=12,
                    ink=True,
                    on_click=lambda _: page.launch_url("https://www.youtube.com/playlist?list=PLfSVB4Wge3DLFBx_RMcCCkeGWhOuDeB3-"),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ["#fefcbf", "#faf089"],
    )

    # Contenedor principal con padding responsivo
    main_content = ft.Container(
        content=ft.Column(
            [
                header,
                ft.Text(
                    "🚀 Proyectos Destacados",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#2d3748",
                ),
                projects_grid,
                support_section,
                playlist_section,
                ft.Container(height=20),  # Espaciado final
            ],
            spacing=30,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=30),
        expand=True,
    )

    page.add(main_content)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

