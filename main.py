

import flet as ft 

class CustomButton(ft.Container): 
    def __init__(self,border_radius, bgcolor, text, data, on_click):
        super().__init__(expand=True) 
        
        self.border_radius = border_radius
        self.width = 2*self.border_radius
        self.height = 2*self.border_radius
        self.bgcolor = bgcolor
        self.data = data
        self.shadow = [
            ft.BoxShadow(
                offset = ft.Offset(15, 15),
                blur_radius = 15,
                color = "#1c9e78",
                blur_style = ft.ShadowBlurStyle.NORMAL,
            ),
            ft.BoxShadow(
                offset = ft.Offset(-15, -15),
                blur_radius = 15,
                color = "#25d7a3",
                blur_style = ft.ShadowBlurStyle.NORMAL,
            ),
        ]
        self.content = ft.Text(value=text, color="black", size=20, weight="bold")
        self.alignment = ft.alignment.center
        self.on_click = on_click
        
def main(page:ft.Page):
    page.bgcolor = "#21bb8e"
    page.padding = 2
    def get_data(e):
        data = e.control.data
        if data == "=":
            try:
                text.value = str(eval(text.value))
            except Exception as e:
                text.value = "ERROR"
        elif data == "C":
            text.value = ""
        elif data == "AC":
            text.value = text.value[:-1] if text.value else text.value
        elif data == "%":
            try:
                text.value = str(float(text.value) / 100)
            except ValueError:
                text.value = "ERROR"
        elif data == ".":
            if not text.value or text.value[-1] not in [".", "+", "-", "/", "*"]:
                text.value += data
        elif data == "±":
            text.value = "-" + text.value if text.value and text.value[0] != "-" else text.value[1:]
        elif data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*"]:
            text.value += data
        page.update()

    text = ft.TextField(read_only=True, border_color="#21bb8e",text_align="right",
                        text_style=ft.TextStyle(size=30, color ="black"))
    
    butons = ft.Column(
        expand = True,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls=[
        ft.Row([
            
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "1", data="1"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "2", data="2"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "3", data="3"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "+", data="+"),

            ],
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            expand=True,
                          
        ),
        ft.Row([
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "4", data="4"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "5", data="5"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "6", data="6"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "-", data="-"),
            ],
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            expand=True,
                            
        ),

        ft.Row([
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "7", data="7"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "8", data="8"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "9", data="9"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "x", data="*"),
            ],
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            expand=True,
                            
        ),

        ft.Row([

            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= ".", data="."),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "0", data="0"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "%", data="%"),
            CustomButton( border_radius=30, bgcolor="#21bb8e", on_click= get_data, text= "÷", data="/"),
            ],
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            expand=True,
                            
        ),

        ft.Row([
            CustomButton( border_radius=25, bgcolor="#21bb8e", on_click= get_data, text= "C", data="C"),
            CustomButton( border_radius=25, bgcolor="#21bb8e", on_click= get_data, text= "⌫", data="AC"),
            CustomButton( border_radius=25, bgcolor="#21bb8e", on_click= get_data, text= "±", data="±"),
            CustomButton( border_radius=25, bgcolor="#21bb8e", on_click= get_data, text= "=", data="="),
            ],
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            expand=True,                  
        ),   
        ],
    )

    text_by = ft.Container(
        padding= ft.padding.only(left=10, top=2, bottom=10, right=10),
        content= ft.Row([
                ft.Text("By: Codlin", style= ft.TextStyle(color="black"))
            ],
            alignment = ft.MainAxisAlignment.SPACE_EVENLY,
            expand=True,    
            spacing = 15,    
        ),
    )
    content = ft.Container(
        expand=True,
        padding= ft.padding.only(top=120, left=10, right=10, bottom=0),
        content=ft.Column(
            expand=True,
            spacing= 0,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            alignment= ft.alignment.center,
            controls=[
            text,
            butons,
            text_by,
        ])
    )
    page.add(content)

ft.app(target=main)


"""
import flet as ft 

conteiner = ft.Container(
    ft.Column([
        ft.Container(
            ft.Text(
                "Iniciar Sesión",
                width=320,
                size=30,
                text_align="center",
                weight="w900"
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Correo electrónico",
                border="underline",
                color="black",
                prefix_icon= ft.icons.EMAIL
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Contraseña",
                border="underline",
                color="black",
                prefix_icon= ft.icons.LOCK,
                password= True
            ),
            padding= ft.padding.only(20,20)
        ),

        ft.Container(
            ft.Checkbox(
                label= "Recordar contraseña",
                check_color= "black"
            ),
             padding= ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                text="INICIAR",
                width=280,
                bgcolor= "black"
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Text("Iniciar sesión con",
                text_align= "center",
                width=320),
        
        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon= ft.icons.EMAIL,
                    tooltip="Google",
                    icon_size=35

                ),
                ft.IconButton(
                    icon= ft.icons.FACEBOOK,
                    tooltip="Facebook",
                    icon_size=35

                ),
                ft.IconButton(
                    icon= ft.icons.APPLE,
                    tooltip="Apple",
                    icon_size=35
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.Row([
                ft.Text("¿No tiene una cuenta?"),
                ft.TextButton("Crear cuenta")               
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20)
        )

    ],
    alignment= ft.MainAxisAlignment.SPACE_EVENLY
    ),


    border_radius= 20,
    width=320,
    height=500,
    gradient= ft.LinearGradient([
        ft.colors.PURPLE,
        ft.colors.PINK,
        ft.colors.RED
    ])
)

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(conteiner)

    
ft.app(target=main)"""
