# -*- coding: utf-8 -*-
import flet as ft
from calc import CalculatorApp

# desde acá se empezará a crear un estilo
# portafolio de los módulos que se irán haciendo
# empezando por Calculadora - calc.py -

def main(page: ft.Page):
    page.title = "Creaciones con Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(e):
        page.views.clear()
        
        # 1. Vista del Menú (SIEMPRE presente)
        page.views.append(
            ft.View(
                "/",
                controls=[
                    ft.AppBar(
                        title=ft.Text("Portafolio de Apps con Flet"), 
                        bgcolor=ft.Colors.BLUE_GREY_900,
                        color=ft.Colors.WHITE
                    ),
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.ElevatedButton(
                            text="Calculadora",
                            bgcolor=ft.Colors.BLUE_ACCENT,
                            color=ft.Colors.WHITE,
                            on_click=lambda _: page.push_route("/calc")
                        )
                    ),
                ],
            )
        )

        # 2. Solo si la ruta es "/calc", agregamos la calculadora encima
        if page.route == "/calc":
            page.views.append(
                ft.View(
                    "/calc",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Calculadora"), 
                            bgcolor=ft.Colors.BLUE_GREY_900,
                            color=ft.Colors.WHITE
                        ),
                        CalculatorApp() 
                    ],
                    padding=0
                )
            )
        
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.push_route(top_view.route)

    # Asignamos los eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Forzamos la ruta raíz "/" para iniciar en el portafolio
    if page.route != "/":
        page.route = "/"
    
    page.push_route(page.route)

if __name__ == "__main__":
    ft.app(target=main)