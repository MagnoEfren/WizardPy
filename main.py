import flet as ft

class Portfolio(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.padding=0
        self.build()


    def build(self):

        self.swicth_mode = ft.IconButton(icon=ft.icons.DARK_MODE, bgcolor="green", on_click=self.change_mode)
 
        self.animation_style = ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT_CUBIC) 

        # Configurando el contenedor
        self.frame_inicio = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(0,0),
            expand=True,
            bgcolor="red"
        )
        self.frame_resumen = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),
            expand=True,
            bgcolor="blue"
        )
        self.frame_trabajo = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),  
            expand=True,
            bgcolor="yellow"
        )

        self.frame_contacto = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),            
            expand=True,
            bgcolor="purple"
        )
        self.frame_sobre_mi = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),            
            expand=True,
            bgcolor="pink"
        )


        self.content = ft.Container(
            expand=True,
            padding=0,
            content= ft.Column(
                expand=True,
                spacing=2,
                controls=[
                    ft.Container(
                        height=200,
                        content = ft.Row(
                                    expand=True,
                                    controls=[
                                    ft.Container(
                                    margin=ft.margin.only(left=20),
                                    content= 
                                    ft.Text(
                                        size=20,
                                        spans=[
                                        ft.TextSpan("Magno", style=ft.TextStyle(color=ft.colors.GREEN_200, weight=ft.FontWeight.W_900)),
                                        ft.TextSpan("Efren", style=ft.TextStyle(color=ft.colors.GREEN_400, weight=ft.FontWeight.W_900)),
                                        ft.TextSpan(".", style=ft.TextStyle(color=ft.colors.GREEN_600, weight=ft.FontWeight.W_900)),
                                            ]
                                        )
                                        ),
                                        ft.ResponsiveRow(
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            expand=True,
                                            controls=[
                                        ft.TextButton("Inicio", style=ft.ButtonStyle(color=ft.colors.GREEN_400),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(0)),
                                        ft.TextButton("Resumen", style=ft.ButtonStyle(color=ft.colors.GREEN_400),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(1)),
                                        ft.TextButton("Trabajo", style=ft.ButtonStyle(color=ft.colors.GREEN_400),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(2)),
                                        ft.TextButton("Contacto", style=ft.ButtonStyle(color=ft.colors.GREEN_400),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(3)),
                                        ft.TextButton("Sobre mi", style=ft.ButtonStyle(color=ft.colors.GREEN_400),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(4)),
                                            ]
                                        ),
                                        ft.Container(
                                            width=50,
                                            margin=ft.margin.only(right=20),
                                            content=self.swicth_mode
                                        )
                                    ]
                                )
                            ),

                    ft.Container(
                        expand=True,
                        bgcolor="black",
                        content= ft.Stack(
                            controls=[
                                self.frame_inicio,
                                self.frame_resumen,
                                self.frame_trabajo,
                                self.frame_contacto,
                                self.frame_sobre_mi,

                            ]
                        )
                    )
                ]
            )
        )




        # Añadiendo el contenedor a la página
        self.page.add(self.content)
    def on_change_page(self, e):
        self.frame_inicio.offset.x = -2
        self.frame_resumen.offset.x = -2
        self.frame_trabajo.offset.x = -2
        self.frame_contacto.offset.x = -2
        self.frame_sobre_mi.offset.x = -2
        if e==0:
            self.frame_inicio.offset.x = 0
        elif e==1:
            self.frame_resumen.offset.x = 0
        elif e==2:
            self.frame_trabajo.offset.x = 0
        elif e==3:
            self.frame_contacto.offset.x = 0
        elif e==4:
            self.frame_sobre_mi.offset.x = 0       
        self.page.update()
    def change_mode(self, e):
        print()
        if e.control.icon =="dark_mode":
            self.swicth_mode.icon = ft.icons.LIGHT_MODE
            self.page.theme_mode = "light"
        else:
            self.swicth_mode.icon = ft.icons.DARK_MODE
            self.page.theme_mode = "dark"
        self.page.update()

# Ejecutando la aplicación pasando directamente la clase Portfolio
ft.app(target=lambda page: Portfolio(page), assets_dir="assets")
