import flet as ft

class Portfolio(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.title = "Mi Portafolio"
        self.font_text = "Tahoma" #Montserrat
        self.page.fonts = {
        "Starjhol": "assets/Starjhol.ttf"
    }

        self.primary_color = ft.colors.GREEN_500
        self.build()


    def build(self):
        self.swicth_mode = ft.IconButton(icon=ft.icons.DARK_MODE, bgcolor=self.primary_color, on_click=self.change_mode)
        self.animation_style = ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT_CUBIC) 

        # Configurando el contenedor
        self.frame_inicio = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(0,0),
            expand=True,
          #  bgcolor="red",
            content= ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        expand=True,
                        controls=[
                                ft.Container(expand=True,
                                            margin=20,
                                            content= ft.Column(
                                                alignment= ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text("Hello I'm",size=30, weight=ft.FontWeight.W_900),
                                                    ft.Text("Nombre Apellido",size=30, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                    ft.Text("Estoy interesado en la creación de aplicaciones de escritorio y movil, la  \n codificación aplicaciones IoT y la enseñanza / tutoría.",size=12, text_align=ft.TextAlign.CENTER),
                                                    ft.Row(expand=True,
                                                           spacing=0,
                                                           alignment= ft.MainAxisAlignment.CENTER,
                                                           controls=[
                                                               ft.TextButton("Descargar CV", 
                                                                    height=40,
                                                                    style=ft.ButtonStyle(
                                                                        elevation = 20,
                                                                        shape=ft.RoundedRectangleBorder(radius=20),
                                                                        side=ft.BorderSide(1, self.primary_color),  
                                                                        overlay_color={"hovered": self.primary_color}
                                                                         ),
                                                                ),
                                                                
                                                               ft.ElevatedButton(content=ft.Image(src="../assets/github.png", fit=ft.ImageFit.COVER, width=20),
                                                                                style=ft.ButtonStyle(
                                                                                shape=ft.CircleBorder(),  
                                                                                overlay_color={"hovered": self.primary_color},
                                                                                side = ft.BorderSide(1, self.primary_color)
                                                                                ),
                                                                                height=40
                                                                                 ),

                                                               ft.ElevatedButton(content=ft.Image(src="../assets/linkedin.png", fit=ft.ImageFit.COVER, width=20),
                                                                                style=ft.ButtonStyle(
                                                                                shape=ft.CircleBorder(),   
                                                                                overlay_color={"hovered": self.primary_color},
                                                                                side = ft.BorderSide(1, self.primary_color)
                                                                                ),
                                                                                height=40
                                                                                 ),
                                                                ft.ElevatedButton(content=ft.Image(src="../assets/youtube.png", fit=ft.ImageFit.COVER, width=20),
                                                                                style=ft.ButtonStyle(
                                                                                shape=ft.CircleBorder(),   
                                                                                overlay_color={"hovered": self.primary_color},
                                                                                side = ft.BorderSide(1, self.primary_color)
                                                                                ),
                                                                                height=40
                                                                                 ),
                                                           ]
                                                           )
                                                ]
                                            )
                                            ),

                                ft.Container(expand=True,
                                        shape=ft.BoxShape.CIRCLE,
                                        clip_behavior= ft.ClipBehavior.HARD_EDGE,
                                        margin=20,
                                        content=ft.Image(src="../assets/foto.jpg",
                                                         ),   

                                             )
                        ]
                    ),
                ]
            )
        )

        self.frame_servicio = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),
            expand=True,
            margin=20,
           content= ft.Column(
               expand=True,
               scroll="auto",
               controls=[
                   ft.ResponsiveRow(
               expand=True,  #Algerian
               spacing=30,
               controls=[
                   ft.Container(expand=True, col = {"md":12, "lg":6},  height=200,
                                padding=10,
                                border=ft.Border(bottom=ft.BorderSide(2, ft.colors.RED_100)), 
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            expand=True,
                                            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ft.Text("01",size=30, weight=ft.FontWeight.W_900,
                                                font_family="Starjhol"),
                                                ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style= ft.ButtonStyle(bgcolor=self.primary_color))
                                            ]
                                        ),
                                        ft.Text("Trabajo 01",size=30, weight=ft.FontWeight.W_900,
                                        ),
                                        ft.Text("La creatividad impulsa cada paso hacia la \n innovación, permitiendo que las ideas \n se transformen en soluciones reales  \n que impactan el mundo de manera significativa.",size=12, 
                                                font_family=self.font_text),  
                                    ]
                                )
                                ),                  
                  
                   ft.Container(expand=True, col = {"md":12, "lg":6},  height=200,
                                padding=10,
                                border=ft.Border(bottom=ft.BorderSide(2, ft.colors.RED_100)), 
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            expand=True,
                                            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ft.Text("02",size=30, weight=ft.FontWeight.W_900,
                                                font_family="Starjhol"),
                                                ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style= ft.ButtonStyle(bgcolor=self.primary_color))
                                            ]
                                        ),
                                        ft.Text("Trabajo 02",size=30, weight=ft.FontWeight.W_900,
                                        ),
                                        ft.Text("La creatividad impulsa cada paso hacia la \n innovación, permitiendo que las ideas \n se transformen en soluciones reales  \n que impactan el mundo de manera significativa.",size=12, 
                                                font_family=self.font_text),  
                                    ]
                                )
                                ),

                   ft.Container(expand=True, col = {"md":12, "lg":6},  height=200,
                                padding=10,
                                border=ft.Border(bottom=ft.BorderSide(2, ft.colors.RED_100)), 
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            expand=True,
                                            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ft.Text("03",size=30, weight=ft.FontWeight.W_900,
                                                font_family="Starjhol"),
                                                ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style= ft.ButtonStyle(bgcolor=self.primary_color))
                                            ]
                                        ),
                                        ft.Text("Trabajo 03",size=30, weight=ft.FontWeight.W_900,
                                        ),
                                        ft.Text("La creatividad impulsa cada paso hacia la \n innovación, permitiendo que las ideas \n se transformen en soluciones reales  \n que impactan el mundo de manera significativa.",size=12, 
                                                font_family=self.font_text),  
                                    ]
                                )
                                ),

                   ft.Container(expand=True, col = {"md":12, "lg":6},  height=200,
                                padding=10,
                                border=ft.Border(bottom=ft.BorderSide(2, ft.colors.RED_100)), 
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            expand=True,
                                            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment= ft.CrossAxisAlignment.CENTER,
                                            spacing=20,
                                            controls=[
                                                ft.Text("04",size=30, weight=ft.FontWeight.W_900,
                                                font_family="Starjhol"),
                                                ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style= ft.ButtonStyle(bgcolor=self.primary_color))
                                            ]
                                        ),
                                        ft.Text("Trabajo 04",size=30, weight=ft.FontWeight.W_900,
                                        ),
                                        ft.Text("La creatividad impulsa cada paso hacia la \n innovación, permitiendo que las ideas \n se transformen en soluciones reales  \n que impactan el mundo de manera significativa.",size=12, 
                                                font_family=self.font_text),  
                                    ]
                                )
                                ),

               ]
           )
               ]
           )
        )

        self.title_resume = ft.Text("Mi Experiencia",size=30, weight=ft.FontWeight.W_900, color=self.primary_color)

        self.container_experience = ft.Container(
            animate_offset=self.animation_style,
            visible=True,
            expand=True,
            content=  ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                spacing=10,
                expand=True,
                controls=[
                    ft.Container(expand=True,
                                content= ft.Row(
                                expand=True,
                                controls=[
                                    ft.Container(
                                        expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                        content= ft.Column(expand=True,
                                                            controls=[
                                                            ft.Text("2020 - Presente",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                            ft.Text("Profesor",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                            ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                            ])

                                    ),

                                    ft.Container(
                                        expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                        content= ft.Column(expand=True,
                                                            controls=[
                                                            ft.Text("2019 - 2020",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                            ft.Text("Desarrollador",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                            ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                            ])
                                    ),
                                ]
                                )
                            ),

                    ft.Container(expand=True,
                                content= ft.Row(
                                expand=True,
                                controls=[
                                ft.Container(
                                    expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                    content= ft.Column(expand=True,
                                                        controls=[
                                                        ft.Text("2017 - 2019",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                        ft.Text("Desarrollador",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                        ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                        ])
                                            ),
                                ft.Container(
                                    expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                    content= ft.Column(expand=True,
                                                            controls=[
                                                            ft.Text("2015 - 2017",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                            ft.Text("Desarrollador",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                            ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                            ])
                                    )
                                ]
                            )                                 
                        ),
                    ]
            )
        )

        self.container_education = ft.Container(
            animate_offset=self.animation_style,
            visible=False,
            expand=True,
            content= ft.Column(
            alignment= ft.MainAxisAlignment.CENTER,
            spacing=10,
            expand=True,
            controls=[
                    ft.Container(expand=True,
                                    content= ft.Row(
                                        expand=True,
                                        controls=[
                                            ft.Container(
                                                expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                                content= ft.Column(expand=True,
                                                                   controls=[
                                                                    ft.Text("2020 - Presente",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                                    ft.Text("Profesor",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                                    ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                                   ])

                                            ),

                                            ft.Container(
                                                expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                                content= ft.Column(expand=True,
                                                                   controls=[
                                                                    ft.Text("2019 - 2020",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                                    ft.Text("Desarrollador",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                                    ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                                   ])
                                            ),
                                        ]
                                    )
                                    ),
                    ft.Container(expand=True,
                                content= ft.Row(
                                    expand=True,
                                    controls=[
                                        ft.Container(
                                            expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                            content= ft.Column(expand=True,
                                                                   controls=[
                                                                    ft.Text("2017 - 2019",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                                    ft.Text("Desarrollador",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                                    ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                                   ])
                                        ),

                                        ft.Container(
                                            expand=True, border_radius=10,bgcolor=ft.colors.with_opacity(0.2, ft.colors.GREEN), padding=20,
                                            content= ft.Column(expand=True,
                                                                   controls=[
                                                                    ft.Text("2015 - 2017",size=18, weight=ft.FontWeight.W_900, color=self.primary_color),
                                                                    ft.Text("Desarrollador",size=12,weight=ft.FontWeight.W_500, color=self.primary_color),
                                                                    ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=10, color=self.primary_color),
                                                                   ])
                                            )
                                        ]
                                    )                                 
                                ),
                    ]
            )
        )

        self.container_skills = ft.Container(
            animate_offset=self.animation_style,
            visible=False,
            expand=True,
            content= ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                spacing=10,
                expand=True,
                controls=[
                    ft.Container(expand=True,
                                 content= ft.Row(
                                     expand=True,
                                     controls=[
                                         ft.Container(
                                             content=ft.Image(src="assets/python.svg"),padding=20,
                                             expand=True, border_radius=10,bgcolor=self.primary_color
                                         ),
                                         ft.Container(
                                             ft.Image(src="assets/matlab.svg"),padding=20,
                                             expand=True, border_radius=10,bgcolor=self.primary_color
                                         ),
                                         ft.Container(
                                             ft.Image(src="assets/js.svg"),padding=20,
                                             expand=True, border_radius=10,bgcolor=self.primary_color
                                         ),

                                     ]
                                 )
                                 ),
                    ft.Container(expand=True,
                                 content= ft.Row(
                                     expand=True,
                                     controls=[
                                         ft.Container(
                                             content=ft.Image(src="assets/html5.svg"),padding=20,
                                             expand=True, border_radius=10,bgcolor=self.primary_color
                                         ),
                                         ft.Container(
                                             ft.Image(src="assets/react.svg"),padding=20,
                                             expand=True, border_radius=10,bgcolor=self.primary_color
                                         ),
                                         ft.Container(
                                             ft.Image(src="assets/solidworks.svg"),padding=20,
                                             expand=True, border_radius=10,bgcolor=self.primary_color
                                         ),

                                     ]
                                 )                                 
                                 ),
                ]
            )
        )


        self.frame_resumen = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),  
            expand=True,
            content= ft.Column(
                expand=True,
                scroll="auto",
                controls=[
                    ft.ResponsiveRow(
                expand=True,
                controls=[
                    ft.Container(
                        expand=True,
                        margin= 20,
                        height=400,

                        alignment= ft.alignment.center,
                        col={"xs": 12,"sm":6},
                        content= ft.Column(
                            expand=True,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                ft.Text("¿Por qué contratarme?",size=30, weight=ft.FontWeight.W_900, color=self.primary_color),
                                ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=12, color=self.primary_color),
                                ft.TextButton("Experiencia",
                                              width=200,
                                              on_click= lambda e: self.on_change_resume(0),
                                              style=ft.ButtonStyle(
                                                    elevation = 20,
                                                    shape=ft.RoundedRectangleBorder(radius=20),
                                                    side=ft.BorderSide(1, self.primary_color),  
                                                        ),
                                            ),

                                ft.TextButton("Educación",
                                              width=200,
                                              on_click= lambda e: self.on_change_resume(1),
                                              style=ft.ButtonStyle(
                                                    elevation = 20,
                                                    shape=ft.RoundedRectangleBorder(radius=20),
                                                    side=ft.BorderSide(1, self.primary_color),  
                                                        ),
                                              ),

                                ft.TextButton("Habilidades",
                                              width=200,
                                              on_click= lambda e: self.on_change_resume(2),
                                              style=ft.ButtonStyle(
                                                    elevation = 20,
                                                    shape=ft.RoundedRectangleBorder(radius=20),
                                                    side=ft.BorderSide(1, self.primary_color),  
                                                        ),
                                              ),


                            ]


                        ),
                        
                    ),

                    ft.Container(
                        expand=True,
                        margin= 20,
                        height=400,
                        col={"xs": 12,"sm":6},
                        content= ft.Column(
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                self.title_resume,
                                ft.Text("La creatividad impulsa cada paso hacia la innovación.",size=12, color=self.primary_color),
                                ft.Stack(
                                    expand=True,
                                    controls=[
                                        self.container_experience,
                                        self.container_education,
                                        self.container_skills,
                                    ]
                                )

                            ]
                        ),
                    )
                ]
            )
                ]
            )
        )


        self.frame_contacto = ft.Container(
            animate_offset=self.animation_style,
            offset=ft.transform.Offset(-2,0),            
            expand=True,
            content= ft.Column(
            expand=True,
            scroll="auto",
            controls=[
                ft.ResponsiveRow(
                expand=True,
                controls=[
                    ft.Container(
                        expand=True,
                        margin= 20,
                        height=400,
                        padding=10,
                        alignment= ft.alignment.center,
                        col={"xs": 12,"sm":6},
                        content= ft.Column(
                            expand=True,
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            alignment= ft.MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                ft.Text("Trabajemos juntos...!",size=20, weight=ft.FontWeight.W_900, color=self.primary_color),
                                ft.TextField(hint_text="Correo electronico", border_radius=30, border_color= self.primary_color),
                                ft.TextField(hint_text="Asunto", border_radius=30, border_color= self.primary_color),
                                ft.TextField(hint_text="Mensaje", border_radius=30, border_color= self.primary_color,
                                            multiline=True,
                                            min_lines=5, 
                                            max_lines=6 
                                             ),
                                ft.ElevatedButton(text ="Enviar",
                                        style=ft.ButtonStyle(overlay_color={"hovered": self.primary_color})) 
                            ]
                        ),
                    ),

                    ft.Container(
                        expand=True,
                        margin= 20,
                        height=400,
                        col={"xs": 12,"sm":6},
                        content= ft.Column(
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            alignment= ft.MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                 ft.Row(controls=[
                                            ft.IconButton(icon=ft.icons.PHONE,
                                                           bgcolor=ft.colors.with_opacity(0.2, self.primary_color)),
                                            ft.Column(spacing=0,
                                                controls=[
                                                          ft.Text("Telefono",size=12, color=self.primary_color),
                                                          ft.Text("+51 123 543 856",size=18, weight= ft.FontWeight.W_500, color=self.primary_color),
                                                      ])
                                        ]),

                                 ft.Row(controls=[
                                            ft.IconButton( #ElevatedButton
                                                icon=ft.icons.MESSAGE,
                                                bgcolor=ft.colors.with_opacity(0.2, self.primary_color)                                           
                                            ),

                                            ft.Column(spacing=0,
                                                controls=[
                                                          ft.Text("Correo electronico",size=12, color=self.primary_color),
                                                          ft.Text("nombre@gmail.com",size=18, weight= ft.FontWeight.W_500, color=self.primary_color),
                                                      ])
                                        ]),

                                 ft.Row(controls=[
                                            ft.IconButton(icon=ft.icons.LOCATION_ON,
                                                           bgcolor=ft.colors.with_opacity(0.2, self.primary_color)  ),
                                            ft.Column(spacing=0,
                                                controls=[
                                                          ft.Text("Dirección",size=12, color=self.primary_color),
                                                          ft.Text("Urb.Manuel G. Jr. XX",size=18, weight= ft.FontWeight.W_500, color=self.primary_color),
                                                      ])
                                        ]),

                            ]
                        ),
                    )
                ]
            )
                ]
            )
        )

        self.content = ft.Container(
            expand=True,
            padding=0,
            content= ft.Column(
                expand=True,
                spacing=2,
                controls=[
                    ft.Container(
                        padding=20,
                        content = ft.Row(
                                    expand=True,
                                    controls=[
                                    ft.Container(
                                    expand=True,
                                    margin=ft.margin.only(left=20),
                                    content= 
                                    ft.Text(
                                        size=20,
                                        spans=[
                                        ft.TextSpan("Nom", style=ft.TextStyle(color=ft.colors.GREEN_100, weight=ft.FontWeight.W_900)),
                                        ft.TextSpan("bre", style=ft.TextStyle(color=ft.colors.GREEN_400, weight=ft.FontWeight.W_900)),
                                        ft.TextSpan(".",style=ft.TextStyle(color=ft.colors.GREEN_800, weight=ft.FontWeight.W_900)),
                                            ]
                                        )
                                        ),
                                        ft.ResponsiveRow(
                                            alignment=ft.MainAxisAlignment.CENTER, 
                                            spacing=0,
                                            run_spacing={"xs": 0},
                                            expand=True,
                                            controls=[
                                        ft.TextButton("Inicio", style=ft.ButtonStyle(color=self.primary_color),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(0)),
                                        ft.TextButton("Servicio", style=ft.ButtonStyle(color=self.primary_color),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(1)),
                                        ft.TextButton("Resumen", style=ft.ButtonStyle(color=self.primary_color),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(2)),
                                        ft.TextButton("Contacto", style=ft.ButtonStyle(color=self.primary_color),col={"xs": 12,"sm":6, "md":2},  on_click= lambda e:self.on_change_page(3)),
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
                        content= ft.Stack(
                            controls=[
                                self.frame_inicio,
                                self.frame_servicio,
                                self.frame_resumen,
                                self.frame_contacto,
                            ]
                        )
                    ),
                    
                    ft.Container(
                    padding=20,
                    gradient= ft.LinearGradient(colors= [self.primary_color, ft.colors.TRANSPARENT], begin=ft.Alignment(y=5, x=0)),
                    alignment=ft.alignment.center,
                    content= ft.Row(
                            expand=True,
                            controls=[
                                ft.Text("© Copyright 2024 Nombre Apellido - Todos los derechos Reservados",size=12,expand=True),
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
        self.frame_servicio.offset.x = -2
        self.frame_resumen.offset.x = -2
        self.frame_contacto.offset.x = -2

        if e==0:
            self.frame_inicio.offset.x = 0
        elif e==1:
            self.frame_servicio.offset.x = 0
        elif e==2:
            self.frame_resumen.offset.x = 0
        elif e==3:
            self.frame_contacto.offset.x = 0
        self.page.update()

    def on_change_resume(self, e):
        self.container_experience.visible = False
        self.container_education.visible = False
        self.container_skills.visible = False

        if e==0:
            self.container_experience.visible = True
            self.title_resume.value = "Mi Experiencia"
        elif e==1:
            self.container_education.visible = True
            self.title_resume.value = "Mi Educación"
        elif e==2:
            self.container_skills.visible = True
            self.title_resume.value = "Mis Habilidades"
        
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
ft.app(target=lambda page: Portfolio(page), assets_dir="assets") #view= ft.WEB_BROWSER,
