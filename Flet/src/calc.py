from dataclasses import field
import flet as ft

@ft.control
class CalcButton(ft.Button):
    expand: int = field(default_factory=lambda: 1)
    style: ft.ButtonStyle = field(
        default_factory=lambda: ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=18),
            padding=ft.padding.all(0) # Padding en 0 para que el texto mande sobre el centro
        )
    )

@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_ACCENT
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY
    color: ft.Colors = ft.Colors.BLACK

@ft.control
class CalculatorApp(ft.Container):
    def init(self):
        self.expression = ""
        
        self.expand = True 
        self.margin = ft.margin.only(left=3, top=25, right=3, bottom=25)
        self.bgcolor = ft.Colors.BLUE_GREY_800
        self.border_radius = ft.BorderRadius.all(25)
        self.padding = 15
        
        self.formula = ft.Text(value="", color=ft.Colors.WHITE60, size=14)
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=35)
        self.preview = ft.Text(value="", color=ft.Colors.GREY_500, size=25)

        self.pad_column = ft.Column(
            expand=True,
            spacing=10, 
            controls=[
                ft.Row(
                    expand=True, 
                    spacing=10,  
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH, 
                    controls=[
                        ExtraActionButton(content=ft.Text("AC", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ExtraActionButton(content=ft.Text("+/-", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ExtraActionButton(content=ft.Text("%", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ActionButton(content=ft.Text("/", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    expand=True,
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        DigitButton(content=ft.Text("7", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        DigitButton(content=ft.Text("8", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        DigitButton(content=ft.Text("9", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ActionButton(content=ft.Text("*", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    expand=True,
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        DigitButton(content=ft.Text("4", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        DigitButton(content=ft.Text("5", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        DigitButton(content=ft.Text("6", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ActionButton(content=ft.Text("-", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    expand=True,
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        DigitButton(content=ft.Text("1", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        DigitButton(content=ft.Text("2", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        DigitButton(content=ft.Text("3", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ActionButton(content=ft.Text("+", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    expand=True,
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        DigitButton(content=ft.Text("0", no_wrap=True, text_align=ft.TextAlign.CENTER), expand=2, on_click=self.button_clicked),
                        DigitButton(content=ft.Text(".", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                        ActionButton(content=ft.Text("=", no_wrap=True, text_align=ft.TextAlign.CENTER), on_click=self.button_clicked),
                    ]
                ),
            ]
        )

        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    expand=15,
                    content=ft.Column(
                        controls=[self.formula, self.preview],
                        alignment=ft.MainAxisAlignment.END,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    ),
                    alignment=ft.Alignment(1.0, 1.0), 
                ),
                ft.Container(
                    expand=20,
                    content=self.result,
                    alignment=ft.Alignment(1.0, 1.0), 
                ),
                ft.Container(
                    expand=65,
                    content=self.pad_column
                )
            ]
        )

    def did_mount(self):
        self.page.on_resize = self.handle_resize
        self.handle_resize(None)

    def handle_resize(self, e):
        width = self.page.width
        height = self.page.height
        
        # MATEMÁTICA DE PROPORCIÓN EXACTA PARA LA ALTURA DEL BOTÓN
        # 1. Calculamos el espacio vertical real restando margin (5x2) y padding (15x2)
        usable_height = height - 40 
        
        # 2. El teclado ocupa el 65% de ese espacio
        keypad_height = usable_height * 0.65 
        
        # 3. Restamos los 4 espacios de 10px entre las 5 filas (40px) y dividimos entre 5
        button_height = (keypad_height - 40) / 5 
        
        # 4. El tamaño de la fuente es estrictamente el 70% de esa altura (minimo 8px por seguridad)
        btn_size = max(8, int(button_height * 0.50))

        # Tamaño del resultado principal basado en el ancho
        if width < 350:
            result_size = 28
        elif width <= 500:
            result_size = 35
        elif width <= 800:
            result_size = 45
        else:
            result_size = 55

        self.result.size = result_size

        for row in self.pad_column.controls:
            for btn in row.controls:
                btn.content.size = btn_size
                btn.update()
        
        self.result.update()

    def button_clicked(self, e):
        data = e.control.content.value
        
        if data == "AC":
            self.expression = ""
            self.result.value = "0"
            self.formula.value = ""
            self.preview.value = ""

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.expression == "" or self.expression == "0":
                if data == ".":
                    self.expression = "0."
                else:
                    self.expression = data
            else:
                self.expression += data
                
            self.result.value = self.expression
            self.update_preview()

        elif data in ("+", "-", "*", "/"):
            if self.expression == "":
                self.expression = "0" + data
            elif self.expression[-1] in ("+", "-", "*", "/"):
                self.expression = self.expression[:-1] + data
            else:
                self.expression += data
                
            self.result.value = self.expression
            self.preview.value = ""

        elif data == "=":
            try:
                res = eval(self.expression)
                res_formatted = self.format_number(res)
                self.formula.value = self.expression + " ="
                self.result.value = str(res_formatted)
                self.preview.value = ""
                self.expression = str(res_formatted)
            except Exception:
                self.result.value = "Error"
                self.expression = ""

        elif data == "%":
            try:
                res = eval(self.expression) / 100
                res_formatted = self.format_number(res)
                self.result.value = str(res_formatted)
                self.expression = str(res_formatted)
                self.update_preview()
            except Exception:
                pass

        elif data == "+/-":
            try:
                res = eval(self.expression) * -1
                res_formatted = self.format_number(res)
                self.result.value = str(res_formatted)
                self.expression = str(res_formatted)
                self.update_preview()
            except Exception:
                pass

        self.update()

    def update_preview(self):
        try:
            if any(op in self.expression for op in ("+", "-", "*", "/")) and self.expression[-1] not in ("+", "-", "*", "/"):
                res = eval(self.expression)
                self.preview.value = f"= {self.format_number(res)}"
            else:
                self.preview.value = ""
        except Exception:
            self.preview.value = ""

    def format_number(self, num):
        try:
            num = float(num)
            if num % 1 == 0:
                return int(num)
            return round(num, 4)
        except:
            return num

def main(page: ft.Page):
    page.title = "Calc App"
    page.padding = 0 
    
    calc = CalculatorApp()
    page.add(calc)

ft.run(main)