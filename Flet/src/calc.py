from dataclasses import field
import flet as ft

@ft.control
class CalcButton(ft.Button):
    expand: int = field(default_factory=lambda: 1)

@ft.control
class DigitButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK

@ft.control
class CalculatorApp(ft.Container):
    def init(self):
        self.expression = ""
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        
        self.formula = ft.Text(value="", color=ft.Colors.WHITE60, size=14)
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=35)
        self.preview = ft.Text(value="", color=ft.Colors.GREY_500, size=18)

        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[self.formula, self.result, self.preview],
                    alignment=ft.MainAxisAlignment.END,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),
                ft.Row(
                    controls=[
                        ExtraActionButton(content="AC", on_click=self.button_clicked),
                        ExtraActionButton(content="+/-", on_click=self.button_clicked),
                        ExtraActionButton(content="%", on_click=self.button_clicked),
                        ActionButton(content="/", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="7", on_click=self.button_clicked),
                        DigitButton(content="8", on_click=self.button_clicked),
                        DigitButton(content="9", on_click=self.button_clicked),
                        ActionButton(content="*", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="4", on_click=self.button_clicked),
                        DigitButton(content="5", on_click=self.button_clicked),
                        DigitButton(content="6", on_click=self.button_clicked),
                        ActionButton(content="-", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(content="1", on_click=self.button_clicked),
                        DigitButton(content="2", on_click=self.button_clicked),
                        DigitButton(content="3", on_click=self.button_clicked),
                        ActionButton(content="+", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(
                            content="0", expand=2, on_click=self.button_clicked
                        ),
                        DigitButton(content=".", on_click=self.button_clicked),
                        ActionButton(content="=", on_click=self.button_clicked),
                    ]
                ),
            ]
        )

    def button_clicked(self, e):
        data = e.control.content
        
        if data == "AC":
            self.expression = ""
            self.result.value = "0"
            self.formula.value = ""
            self.preview.value = ""

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            # Evitar ceros a la izquierda
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
            # Si el último carácter ya es un operador, lo reemplazamos
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
            # Solo evalúa si hay operadores en la cadena y no termina en uno
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
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    calc = CalculatorApp()
    page.add(calc)

ft.run(main)