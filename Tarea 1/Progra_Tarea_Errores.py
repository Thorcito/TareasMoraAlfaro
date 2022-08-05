# Programacion realizada por Nadir Alfaro y Randy Mora

# Los códigos de error utilizados son los siguientes
# 0 = No hay error
# E1 = Error cuando alguno de los operandos o el operador no es de tipo int
# E2 = Error cuando se escoge un op diferente a 1, 2 o 3
# E3 = Error cuando se intenta dividir entre 0
# E4 = Error cuando la entrada no es string

# Variable global
zero = 0  # Variable usada en la función cero


# Funciones de operaciones


def Sumatoria(op1, op2):  # Función de suma
    res = op1 + op2  # Se guarda la suma en res
    return res  # Retorna resultado


def Resta(op1, op2):  # Función de resta
    res = op1 - op2  # Se realiza una resta
    return res  # Retorna resultado


def Division(op1, op2):  # Función de división
    res = op1 / op2  # Se realiza una división
    return res  # Retorna resultado


# Manejo de error al dividir entre 0
def Cero(op2):
    global zero  # Se llama a la variable global
    if op2 == 0:  # Caso en donde el operando es 0
        zero = 1  # Cambia el valor de la variable global
        return zero  # Retorna la variable
    else:  # En caso de que op2 no sea 0 se cambia el
        # valor de la variable global
        zero = 0
        return zero  # Retorna la variable


# Función para hacer las operaciones correspondientes


def basic_operations(op1, op2, op):
    global zero  # Se llama la variable global
    Cero(op2)  # Se llama la función Cero
    # Se verifica si todos los datos ingresados son enteros
    if isinstance(op1, int) & isinstance(op2, int) & isinstance(op, int):
        if op == 1:  # En caso de que op sea 1
            return Sumatoria(op1, op2)  # Se llama la función de suma
        elif op == 2:  # En caso de que op sea 2
            return Resta(op1, op2)  # Se llama la función de resta
        elif op == 3:  # Caso en que op sea 3
            if zero == 0:  # Se verifica el valor de la variable global
                return Division(op1, op2)  # Se llama a la función de dividir
            else:  # En caso de que el op2 sea 0, retorna el error E3
                return "E3"
        else:  # En caso de que la operación sea diferente a 1, 2 o 3
            return "E2"  # retorna el error E2
    else:  # Si los valores no son enteros, retorna el error E1
        return "E1"


# Función para contar caracteres de un string


def count_char(entrada):
    cont = 0  # Variable usada como contador
    if isinstance(entrada, str):  # Se verifica si la entrada es una string
        while entrada[cont:]:  # Ciclo para contar
            cont += 1  # Se suma el número de caracteres
        return cont  # Retorna el contador
    else:  # En caso  de que la entrada no sea un string retorna el error E4
        return "E4"
