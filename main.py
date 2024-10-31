import flet as ft 

class UI(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.expand = True
        self.page.fonts={"Starjhol":"../assets/Starjhol.ttf",}
        self.tx='Tahoma'
        self.page.title='Cristian Yancis'
        self.page.route='/'
        
        
        self.color_p = ft.colors.RED_800
        self.color_s = ft.colors.BLUE_800  
        
        self.build()

    def build(self):
        self.switch = ft.IconButton(
            tooltip='Tema ',
            icon=ft.icons.LIGHT_MODE,
            bgcolor=self.color_p,
            icon_color=ft.colors.WHITE,
            on_click=self.mod_ui
        
        )
        self.text=ft.Text(size=15,value='Yo me especializo en desarrollo de aplicaciones trabajando con las siguientes tecnologías: JavaScript, Python, Java, React, SQL y Robótica con Arduino',)
        self.title=ft.Text('Tecnologías',size=30,weight=ft.FontWeight.W_900,color=self.color_p)
        
        self.animetion_style = ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT_CUBIC)
        self.frame_exp = ft.Container(expand=True,visible=False, 
                                      content=ft.Column(
                                          alignment= ft.MainAxisAlignment.CENTER,
                                          spacing=25
                                          ,expand=True
                                          ,controls=[
                                              ft.Container( # inicio 
                                                expand=True,
                                                content=ft.Row(
                                                    expand=True,
                                                    controls=[                                                        
                                                        ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('Julio - Agosto 2024', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('André Ampere', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Hice una app de escritorio para asistencia automatica con un codigo de barra', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )
                                                        ,ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('Septiembre - Octubre 2024', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('VIA Asesores S.A', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Hice mis practicas profecionales profecionales ', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )     
                                                    ]
                                                )
                                            ) # fin
                                            ,ft.Container( # inicio 
                                                expand=True,
                                                content=ft.Row(
                                                    expand=True,
                                                    controls=[                                                        
                                                        ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('Año', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('Empresa', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Descripción ', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )
                                                        ,ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('Año', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('Empresa', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Descripción ', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )     
                                                    ]
                                                )
                                            ) # fin
                                          ]
                                      ))
        self.frame_formacion = ft.Container(expand=True,visible=False,
                                            content=ft.Column(
                                          alignment= ft.MainAxisAlignment.CENTER,
                                          spacing=25
                                          ,expand=True
                                          ,controls=[
                                              ft.Container( # inicio 
                                                expand=True,
                                                content=ft.Row(
                                                    expand=True,
                                                    controls=[                                                        
                                                        ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('2013 - 2019', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('Liceo Cristiano Monte Sinaí', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Estudios de Nivel Primario', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )
                                                        ,ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('2020 - 2022', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('Liceo Cristiano Monte Sinaí', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Estudios de Nivel Básico', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )     
                                                    ]
                                                )
                                            ) # fin
                                            ,ft.Container( # inicio 
                                                expand=True,
                                                content=ft.Row(
                                                    expand=True,
                                                    controls=[                                                        
                                                        ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('2023-2024', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('Tecnologico Industrial André Ampere', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Estudie mi carrera de nivel medio como Bachiller en computación', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )
                                                        ,ft.Container(
                                                            expand=True,
                                                            padding=15,
                                                            border_radius=10,
                                                            bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_100),
                                                            border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),
                                                            content=ft.Column(
                                                                controls=[
                                                                    ft.Text('Año', size=20, weight=ft.FontWeight.W_900),
                                                                    ft.Text('institucion', size=18, weight=ft.FontWeight.W_100),
                                                                    ft.Text('Descripción ', size=15, font_family=self.tx),
                                                                ]
                                                            )
                                                        )     
                                                    ]
                                                )
                                            ) # fin
                                          ]
                                      )
                                    )
        self.frame_tecnologias= ft.Container(expand=True,visible=True,
                                             content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                spacing=10, 
                                                expand=True,
                                                controls=[
                                                    ft.Container(expand=True
                                                                ,content=ft.Row(expand=True,
                                                                                controls=[
                                                                                    ft.Container(padding=20,expand=True,border_radius=10,bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),content=ft.Image(src='../assets/svg/javascript.svg',width=100)),
                                                                                    ft.Container(padding=20,expand=True,border_radius=10,bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),content=ft.Image(src='../assets/svg/python.svg',width=100)),
                                                                                    ft.Container(padding=20,expand=True,border_radius=10,bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),content=ft.Image(src='../assets/svg/java.svg',width=100))
                                                                ]
                                                            )
                                                        ),
                                                    ft.Container(expand=True
                                                                ,content=ft.Row(expand=True,
                                                                                controls=[
                                                                                    ft.Container(padding=20,expand=True,border_radius=10,bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),content=ft.Image(src='../assets/svg/react.svg',width=100)),
                                                                                    ft.Container(padding=20,expand=True,border_radius=10,bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),content=ft.Image(src='../assets/svg/db.svg',width=100)),
                                                                                    ft.Container(padding=20,expand=True,border_radius=10,bgcolor=ft.colors.with_opacity(0.2,ft.colors.BLUE_GREY_200),border=ft.Border(left=ft.BorderSide(2, color=self.color_p)),content=ft.Image(src='../assets/svg/arduino.svg',width=100))
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            )

        
        # Frames inicializados y añadidos a la lista para fácil manipulación       
        self.frames_in=ft.Container(expand=True, animate_offset=self.animetion_style, offset=ft.transform.Offset(0, 0)
                         ,content=ft.Row(expand=True,
                            
                            controls=[
                                ft.Container(
                                    margin=20
                                    ,expand=True
                                    ,content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER
                                        ,horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                        ,controls=[
                                            ft.Text('Hola, soy',size=30,weight=ft.FontWeight.W_900)
                                            ,ft.Text('Cristian Bernardo Yancis Ajuchán',size=30,weight=ft.FontWeight.W_900, color=self.color_p)
                                            ,ft.Text('Estoy interesado en la creación de aplicaciones de escritorio y móvil, el desarrollo de aplicaciones y páginas web, el análisis de datos y el machine learning.',size=15)
                                            
                                            ,ft.Row(
                                                     spacing=0
                                                    ,controls=[
                                                        ft.TextButton('Descargar CV'                                                                
                                                                      ,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(20),side=ft.BorderSide(1,self.color_p),overlay_color={'hovered':self.color_p}))
                                                        ,ft.ElevatedButton(
                                                                        tooltip='GitHub'
                                                                        ,content=ft.Image(
                                                                            src='../assets/github.png'
                                                                            ,fit=ft.ImageFit.COVER
                                                                            ,width=20
                                                                            
                                                                        )
                                                                        ,style=ft.ButtonStyle(shape=ft.CircleBorder(),overlay_color={'hovered':self.color_p},side=ft.BorderSide(1,self.color_p))
                                                                        ,height=40
                                                                        ,on_click=lambda e: self.link(0)
                                                                    )
                                                        ,ft.ElevatedButton(
                                                                        tooltip='Linkedin'
                                                                        ,content=ft.Image(
                                                                            src='../assets/in.png'
                                                                            ,fit=ft.ImageFit.COVER
                                                                            ,width=20
                                                                        )
                                                                        ,style=ft.ButtonStyle(shape=ft.CircleBorder(),overlay_color={'hovered':self.color_p},side=ft.BorderSide(1,self.color_p))
                                                                        ,height=40
                                                                        ,on_click=lambda e: self.link(1)
                                                                    ),
                                                        ft.ElevatedButton(
                                                                        tooltip='YouTube'
                                                                        ,content=ft.Image(
                                                                            src='../assets/ytube.png'
                                                                            ,fit=ft.ImageFit.COVER
                                                                            ,width=20
                                                                            
                                                                        )
                                                                        ,style=ft.ButtonStyle(shape=ft.CircleBorder(),overlay_color={'hovered':self.color_p},side=ft.BorderSide(1,self.color_p))
                                                                        ,height=40
                                                                        ,on_click=lambda e: self.link(2)
                                                                    )
                                                        
                                                    ]
                                                    )
                                        ]
                                    )
                                )
                                ,ft.Container(
                                    expand=True
                                    ,shape=ft.BoxShape.CIRCLE
                                    ,clip_behavior=ft.ClipBehavior.ANTI_ALIAS
                                    ,margin=50
                                    ,shadow=ft.BoxShadow(spread_radius=50,blur_radius=50,color=self.color_p)
                                    ,content=ft.Image(src='../assets/log.png')
                                )
                            ]
                )
            )
          
        self.frame_servicio=ft.Container(expand=True, animate_offset=self.animetion_style, offset=ft.transform.Offset(-2, 0),
                    content=ft.Column(  # Cambiamos `content=[...]` a `content=ft.Column([...])`
                        scroll='auto',
                        expand=True,
                        controls=[
                            ft.ResponsiveRow(
                                expand=True,
                                spacing=20,
                                controls=[
                                    ft.Container(  # cuadro
                                        margin=20, expand=True, col={'md': 12, 'lg': 6}, height=200, padding=10, border=ft.Border(bottom=ft.BorderSide(2, color=self.color_p)),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    expand=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=20,
                                                    controls=[
                                                        ft.Text('01', size=30, weight=ft.FontWeight.W_900, font_family='Starjhol'),
                                                        ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style=ft.ButtonStyle(bgcolor=self.color_p)),
                                                    ]
                                                ),
                                                ft.Row(controls=[ft.Icon(ft.icons.WEB_ASSET,size=40,color=self.color_s),ft.Text('Páginas Web', size=30, weight=ft.FontWeight.W_900)]),
                                                ft.Text(size=15, value='Desarrollo de páginas web estáticas con React, \ncon HTML, CSS y JavaScript de manera responsiva', font_family=self.tx)
                                            ]
                                        )
                                    ),
                                    ft.Container(  # cuadro 2
                                        margin=20, expand=True, col={'md': 12, 'lg': 6}, height=200, padding=10, border=ft.Border(bottom=ft.BorderSide(2, color=self.color_p)),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    expand=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=20,
                                                    controls=[
                                                        ft.Text('02', size=30, weight=ft.FontWeight.W_900, font_family='Starjhol'),
                                                        ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style=ft.ButtonStyle(bgcolor=self.color_p)),
                                                    ]
                                                ),ft.Row(
                                                    controls=[ft.Icon(ft.icons.WEB,size=40,color=self.color_s),ft.Text('Aplicaciones Web', size=30, weight=ft.FontWeight.W_900),]
                                                    ),
                                                
                                                ft.Text(size=15, value='Desarrollo de aplicaciones web con React, \nJavaScript, Next.js, Node.js y Flet de Python de manera responsiva', font_family=self.tx)
                                            ]
                                        )
                                    ),
                                    ft.Container(  # cuadro
                                        margin=20, expand=True, col={'md': 12, 'lg': 6}, height=200, padding=10, border=ft.Border(bottom=ft.BorderSide(2, color=self.color_p)),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    expand=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=20,
                                                    controls=[
                                                        ft.Text('03', size=30, weight=ft.FontWeight.W_900, font_family='Starjhol'),
                                                        ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style=ft.ButtonStyle(bgcolor=self.color_p)),
                                                    ]
                                                ),
                                                ft.Row(controls=[ft.Icon(ft.icons.SMARTPHONE,size=40,color=self.color_s),ft.Text('Aplicaciones Móviles', size=30, weight=ft.FontWeight.W_900)]),
                                                ft.Text(size=15, value='Desarrollo de aplicaciones móviles con Flet de Python, \nJava y React', font_family=self.tx)
                                            ]
                                        )
                                    ),
                                    ft.Container(  # cuadro
                                        margin=20, expand=True, col={'md': 12, 'lg': 6}, height=200, padding=10, border=ft.Border(bottom=ft.BorderSide(2, color=self.color_p)),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    expand=True, alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=20,
                                                    controls=[
                                                        ft.Text('04', size=30, weight=ft.FontWeight.W_900, font_family='Starjhol'),
                                                        ft.IconButton(icon=ft.icons.ARROW_OUTWARD, style=ft.ButtonStyle(bgcolor=self.color_p)),
                                                    ]
                                                ),
                                                ft.Row(controls=[ft.Icon(ft.icons.LAPTOP ,size=40 ,color=self.color_s),ft.Text('Aplicaciones de Escritorio', size=30, weight=ft.FontWeight.W_900)]),
                                                ft.Text(size=15, value='Desarrollo de aplicaciones de escritorio con Java, \nFlet y Tkinter de Python', font_family=self.tx)
                                            ]
                                        )
                                    )

                                ]
                            )
                        ]
                    )
            )

        self.frame_resumen=ft.Container(expand=True, animate_offset=self.animetion_style, offset=ft.transform.Offset(-2, 0),
                content=ft.Column( expand=True, scroll='auto',
                    controls=[
                        ft.ResponsiveRow(expand=True,
                            controls=[
                                ft.Container(expand=True, margin=20, height=500, alignment=ft.alignment.center,col={'xs': 12, 'sm': 6},
                                    content=ft.Column(expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        controls=[
                                            ft.Text('¿Por qué contratarme?', size=30, weight=ft.FontWeight.W_900, color=self.color_p),
                                            ft.Text('razón aquí', size=15, font_family=self.tx),
                                            ft.ElevatedButton('Tecnologías',on_click=lambda e: self.info(2),width=200,style=ft.ButtonStyle(elevation=20,shape=ft.RoundedRectangleBorder(radius=20),side=ft.BorderSide(1,color=self.color_p),overlay_color={'hovered':self.color_p})),
                                            ft.ElevatedButton('Experiencia',on_click=lambda e: self.info(0),width=200,style=ft.ButtonStyle(elevation=20,shape=ft.RoundedRectangleBorder(radius=20),side=ft.BorderSide(1,color=self.color_p),overlay_color={'hovered':self.color_p},)),
                                            ft.ElevatedButton('Educación ',on_click=lambda e: self.info(1),width=200,style=ft.ButtonStyle(elevation=20,shape=ft.RoundedRectangleBorder(radius=20),side=ft.BorderSide(1,color=self.color_p),overlay_color={'hovered':self.color_p},)),
                                        ]
                                    )
                                ),
                                # Segundo contenedor (puedes añadir contenido o ajustes si es necesario)
                                ft.Container(expand=True,margin=20,height=500,col={'xs': 12, 'sm': 6}
                                             ,content=ft.Column(
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                                ,expand=True,
                                                 controls=[
                                                    self.title
                                                    ,self.text
                                                    ,ft.Stack(
                                                        expand=True,
                                                        controls=[
                                                            self.frame_exp,
                                                            self.frame_formacion,
                                                            self.frame_tecnologias
                                                        ]
                                                        )
                                                    ]
                                             )
                                              
                                             )  
                            ]
                        )
                    ]
                )
            )

        self.frame_contact=ft.Container(expand=True, bgcolor=ft.colors.PURPLE, animate_offset=self.animetion_style, offset=ft.transform.Offset(-2, 0)
                                        
                                        )
        
        self.contenido = ft.Column(
            expand=True,
            spacing=2,
            controls=[
                ft.Container(  # header
                    padding=20,
                    content=ft.Row(
                        expand=True,
                        controls=[
                            ft.Container(
                                expand=True,
                                margin=ft.margin.only(left=20),
                                content=ft.Text(
                                    size=23,
                                    spans=[
                                        ft.TextSpan('Cris', style=ft.TextStyle(color=ft.colors.RED_100, weight=ft.FontWeight.W_900)),
                                        ft.TextSpan('tian', style=ft.TextStyle(color=ft.colors.RED_400, weight=ft.FontWeight.W_900)),
                                        ft.TextSpan('.', style=ft.TextStyle(color=ft.colors.RED_900, weight=ft.FontWeight.W_900)),
                                    ]
                                )
                            ),
                            ft.ResponsiveRow(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=0,
                                expand=True,
                                controls=[
                                    ft.TextButton('Inicio', style=ft.ButtonStyle(color=self.color_p), col={'xs': 12, 'sm': 6, 'md': 3}, on_click=lambda e: self.change(0)),
                                    ft.TextButton('Servicio', style=ft.ButtonStyle(color=self.color_p), col={'xs': 12, 'sm': 6, 'md': 3}, on_click=lambda e: self.change(1)),
                                    ft.TextButton('Resumen', style=ft.ButtonStyle(color=self.color_p), col={'xs': 12, 'sm': 6, 'md': 3}, on_click=lambda e: self.change(2)),
                                    ft.TextButton('Contacto', style=ft.ButtonStyle(color=self.color_p), col={'xs': 12, 'sm': 6, 'md': 3}, on_click=lambda e: self.change(3)),
                                ]
                            ),
                            ft.Container(
                                width=50,
                                margin=ft.margin.only(right=20),
                                content=self.switch
                            )
                        ]
                    )
                ),
                ft.Container(  # body
                    expand=True,
                    content=ft.Stack(
                        
                        controls=[
                            self.frames_in,
                            self.frame_servicio,
                            self.frame_resumen,
                            self.frame_contact
                        ]
                    )
                ),
                ft.Container(  # footer
                    padding=20,
                    gradient=ft.LinearGradient(colors=[self.color_p, ft.colors.TRANSPARENT]),
                    content=ft.Text('Copyright 2024 Cristian Yancis - Todos los derechos reservados', size=14)
                )
            ]
        )
        self.page.add(self.contenido)
    
    def info(self, e):
        self.frame_exp.visible = False
        self.frame_formacion.visible = False
        self.frame_tecnologias.visible = False
        if e == 0:
            self.frame_exp.visible =True
            self.title.value = 'Mi Experiencia'
            self.text.value='mi experiencia laboral muy breve y me gustaria ganar más experiencia con ustedes'
            self.page.title = 'Experiencia'
            self.page.route='/resumen/experiencia'
        elif e == 1:
            self.frame_formacion.visible = True
            self.title.value = 'Educación'
            self.text.value='Mis estudios fueron en las siguientes intituciones'
            self.page.title = 'Educación'
            self.page.route='/resumen/educacion'
        elif e == 2:
            self.frame_tecnologias.visible = True
            self.title.value = 'Tecnologías'
            self.text.value='Yo me especializo en desarrollo de aplicaciones trabajando con las siguientes tecnologías: JavaScript, Python, Java, React, SQL y Robótica con Arduino'
            self.page.title='Tecnologías'
            self.page.route='/resumen/tecnologias'
        self.page.update()
    
    # Cambio de página
    def change(self, e ):
        self.frames_in.offset.x = -2
        self.frame_servicio.offset.x = -2 
        self.frame_resumen.offset.x = -2
        self.frame_contact.offset.x = -2 

        if e==0 :
            self.frames_in.offset.x = 0
            self.page.title='Cristian Yancis'
            self.page.route='/'
        elif e==1:
            self.frame_servicio.offset.x = 0
            self.page.title='Servicio'
            self.page.route='/servicio'
        elif e==2:
            self.frame_resumen.offset.x = 0
            self.page.title='Resumen'
            self.page.route='/resumen'
        elif e==3:
            self.frame_contact.offset.x = 0
            self.page.title='Contacto'
            self.page.route='/contacto'

        self.page.update()

    # Cambio de tema de la UI
    def mod_ui(self, e):
        self.page.theme_mode = 'light' if self.page.theme_mode == 'dark' else 'dark'
        self.switch.icon = ft.icons.DARK_MODE if self.page.theme_mode == 'light' else ft.icons.LIGHT_MODE
        self.page.update()
        
    def link(self, e):
        if e==0:
            self.page.launch_url('https://github.com/morris3432') 
        elif e==1:
            self.page.launch_url('www.linkedin.com/in/cristian-bernardo-yancis-ajuchán-32717a306')
        elif e==2:
            self.page.launch_url('https://www.youtube.com/@cristianyancis8464')
        elif e==3:
            #self.page.launch_url('https://www.facebook.com/cristian.yancis.morris')
            print(e)

def main(page: ft.Page):
   UI(page)

ft.app(target=main,assets_dir='assets')
