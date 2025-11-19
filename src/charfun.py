"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.

Última Modificación: 
Autor: Franco Lionel Zalokar
Dependencias: unicodedata
"""

from modulo1.funciones import esPalindromo 

def main():
    while True:
        frase = input("Introduce una frase (o 'salir' para terminar): ")

        if frase.lower() == "salir":
            print("Programa finalizado.")
            break

        if esPalindromo(frase):
            print("La frase es palíndroma.")
        else:
            print("La frase no es palíndroma.")

if __name__ == "__main__":
    main()