# Programacion realizada por Nadir Alfaro y Randy Mora

# este es el archivo para realizar las pruebas

# se importan las funciones definidas en Progra_Tarea1

from Progra_Tarea1 import basic_operations
from Progra_Tarea1 import count_char

#test para verificar que se realiza la suma de manera satisfactoria
def test_suma():
    a = 3
    b = 5
    ope = 1
    assert basic_operations(a, b, ope) == 8

#test para verificar que se realiza la resta de manera satisfactoria
def test_resta():
    a = 2
    b = 6
    ope = 2
    assert basic_operations(a, b, ope) == -4

#test para verificar que se realiza la division de manera satisfactoria
def test_division():
    a = 9
    b = 3
    ope = 3
    assert basic_operations(a, b, ope) == 3

#test para verificar cuando el operando es string tire el error correspondiente
def test_string():
    a = "ab"
    b = 5
    ope = 1
    assert basic_operations(a, b, ope) == "E1"

#test para verificar cuando el operador es string tire el error correspondiente
def test_string2():
    a = 3
    b = "ab"
    ope = 1
    assert basic_operations(a, b, ope) == "E1"

#test para verificar cuando la operacion es string tire el error correspondiente
def test_string3():
    a = 3
    b = 5
    ope = "ab"
    assert basic_operations(a, b, ope) == "E1"

#test para verificar cuando se intente dividir entre 0 si tira el error correspondiente
def test_division_error():
    a = 3
    b = 0
    ope = 3
    assert basic_operations(a, b, ope) == "E3"

#test para verificar si la funcion cuenta la cantidad correcta de caracteres en el string
def test_cunta_letras():
    a = "abcdefghijk"
    assert count_char(a) == 11

#test para verificar si la funcion cuenta la cantidad correcta de caracteres incluyendo espacios en el string
def test_cunta_letras2():
    a = "abcdef ghijk"
    assert count_char(a) == 12

#test para verificar si la funcion retorna el error correspondiente cuando no se le ingresa un string
def test_no_string():
    a = 44
    assert count_char(a) == "E4"

#test para verificar si retorna el error correspondiente cuando se selecciona un operando invalido
def test_wrong_ope():
    a = 3
    b = 0
    ope = 4
    assert basic_operations(a, b, ope) == "E2"