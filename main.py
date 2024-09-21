import sly
import re

class Lexer(sly.Lexer):

    tokens = {A,B,C}
    A = r'a+'
    B = r'b|c'
    C = r'd+'

    def __init__(self):
        self.patron = f'^{self.A}({self.B}){self.C}$'

    def validar_cadena(self, cadena):
        return bool(re.match(self.patron, cadena))

lexer = Lexer()

cadenas_prueba = input("Cadena de prueba: ")


if lexer.validar_cadena(cadenas_prueba):
    print(f"'{cadenas_prueba}' cumple con el lenguaje")
else:
    print(f"'{cadenas_prueba}' no cumple con el lenguaje")
