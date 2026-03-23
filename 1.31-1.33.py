'''
Ejercicio:
“Analizador de Conjuntos y Números Naturales”

Objetivo
Practicar la creación y uso de funciones en Python (por ejemplo, len(), funciones propias con def, y f-strings) mientras refuerzas los conceptos de Baldor sobre coordinación de conjuntos
y el origen de los números naturales.

Consigna
Imagina que tienes tres conjuntos representados como strings:

"A,B,C"

"X,Y,Z"

"1,2,3,4"

Tu tarea es escribir un programa en Python que:

-Defina funciones para analizar estos conjuntos.

-Una función que calcule cuántos elementos tiene cada conjunto (usando len() sobre la lista).

-Otra función que muestre si dos conjuntos son coordinables (misma cantidad de elementos).

-Una función que muestre cómo se construye la sucesión fundamental (añadiendo un elemento al conjunto anterior).

Aplique los caracteres de coordinación:

Carácter idéntico: muestra que un conjunto es coordinable consigo mismo.

Carácter recíproco: si A ↔ B, entonces B ↔ A.

Carácter transitivo: si A ↔ B y B ↔ C, entonces A ↔ C.

Relacione con el número natural:

Usa una función que muestre cómo el número de elementos de un conjunto corresponde a un número natural.
==================================================================================================================
Niveles de abordaje sugeridos                                              

Forma básica (conceptos básicos + nuevo):

Declara variables con los conjuntos como strings.
Usa split para convertirlos en listas.
Aplica len() directamente en cada lista y muestra el resultado con print.
======================================================================================
Forma intermedia (conceptos intermedios + nuevo):

Define funciones con def para calcular la longitud y verificar si dos conjuntos son coordinables.
Usa f-strings para mostrar resultados más claros.
Implementa el carácter idéntico y recíproco con condicionales (if).
======================================================================================

Forma avanzada (conceptos avanzados + nuevo):

Crea una función que genere automáticamente la sucesión fundamental de conjuntos (añadiendo elementos paso a paso).
Usa bucles para mostrar cómo se construyen los conjuntos y cómo se relacionan con los números naturales.
Implementa el carácter transitivo verificando tres conjuntos distintos.
=========================================================================================
Resultado esperado (ejemplo conceptual, no código)
Código
Conjunto A tiene 3 elementos → Número natural 3
Conjunto B tiene 3 elementos → Número natural 3
Conjunto C tiene 4 elementos → Número natural 4

Carácter idéntico:
A ↔ A

Carácter recíproco:
A ↔ B y B ↔ A

Carácter transitivo:
A ↔ B, B ↔ C → A ↔ C

Sucesión fundamental:
{A}, {A,B}, {A,B,C}, {A,B,C,D} ...
'''
'''
==============================================================================
Forma básica (conceptos básicos + nuevo):    

Declara variables con los conjuntos como strings.
Usa split para convertirlos en listas.
Aplica len() directamente en cada lista y muestra el resultado con print.
===============================================================================
'''

print("Forma Basica\n","=" * 40)

letras_1 = "A,B,C"

letras_2 = "X,Y,Z"

numeros = "1,2,3,4"

lista_letras = letras_1.split(",")
lista_letras_2 = letras_2.split(",")
lista_numeros = numeros.split(",")


print("El conjunto A tiene ->", len(lista_letras), "elementos", "->" ,"Numero natural", len(lista_letras))
print("El conjunto B tiene ->", len(lista_letras_2), "elementos", "->" ,"Numero natural", len(lista_letras_2))
print("El conjunto C tiene ->", len(lista_numeros), "elementos", "->" ,"Numero natural", len(lista_numeros))
print("=" *40)

print("Forma Intermedia\n","=" * 40)
'''
Forma intermedia (conceptos intermedios + nuevo):

Define funciones con def para calcular la longitud y verificar si dos conjuntos son coordinables.
Usa f-strings para mostrar resultados más claros.
Implementa el carácter idéntico y recíproco con condicionales (if).
'''
def calculo_longitud_conjuntos():
    '''
    Funcion que permite calcular la longitud de conjuntos.
    '''
    elem_letras_1 = len(lista_letras)
    elem_letras_2 = len(lista_letras_2)
    elem_numeros = len(lista_numeros)

    return elem_letras_1, elem_letras_2, elem_numeros

cantidad = calculo_longitud_conjuntos()

def verificacion_de_coordinacion(cantidad):
    '''
    Funcion que verifica coordinacion entre los conjuntos
    '''
    a,b,c = cantidad
    
    print("Carácter idéntico: A ↔ A")
    print("Carácter idéntico: B ↔ B")
    print("Carácter idéntico: C ↔ C")


    if a == b:
        print("Carácter recíproco: A ↔ B y B ↔ A")
    else:
        print("El conjunto A no es coordinable con el conjunto B.")
    if b == c:
        print("Carácter recíproco: B ↔ C y C ↔ B")
    else:
        print ("El conjunto B no es coordinable con el conjunto C.")

print(f"El conjunto A tiene -> {cantidad[0]} elementos. Numero natural ->{cantidad[0]}")
print(f"El conjunto B tiene -> {cantidad[1]} elementos. Numero natural ->{cantidad[1]}")
print(f"El conjunto C tiene -> {cantidad[2]} elementos. Numero natural ->{cantidad[2]}")
verificacion_de_coordinacion(cantidad)

print("=" * 40)

print("Forma Avanzada\n","=" * 40)
'''
Forma avanzada (conceptos avanzados + nuevo):

Crea una función que genere automáticamente la sucesión fundamental de conjuntos (añadiendo elementos paso a paso).
Usa bucles para mostrar cómo se construyen los conjuntos y cómo se relacionan con los números naturales.
Implementa el carácter transitivo verificando tres conjuntos distintos.
'''

def sucesion_fundamental(n): #Funcion con un parametro de control n # Defines la función con un parámetro de control 'n'

    #Funcion que genera la sucesion fundamental de conjuntos (anhade elementos paso a paso)
    # Comentario: la función recibe 'n' y genera la sucesión fundamental de conjuntos

    
    conjunto = [] #Conjunto vacio que servira como acumulador/ # Inicializas una lista vacía, que representa el conjunto nulo (sin elementos)

    print(f"Conjunto nulo {conjunto}") # Imprimes el conjunto vacío, mostrando explícitamente el conjunto nulo ↔ número natural 0

    for i in range(n): # Inicias un bucle que se repetirá 'n' veces, con 'i' como variable de iteración (0,1,...,n-1)

        conjunto.append(i + 1) # En cada vuelta añades un nuevo elemento a la lista; usas 'i+1', por lo que el primer valor añadido es 1
        print(f"Conjunto con {len(conjunto)} elementos <-> numero natural {len(conjunto)} = {conjunto}")
         # Aquí tu lista va creciendo paso a paso, acumulando los elementos


sucesion_fundamental(10)

#CODIGO HECHO POR LA IA YA QUE NO SUPE EN ESTE MOMENTO COMO REALIZARLO

# Definimos una función llamada verificar_transitividad que recibe tres conjuntos (listas) como parámetros

def verificar_transitividad(A, B, C):
    
    # Verificamos si los tres conjuntos tienen la misma longitud
    # La condición es: A coordina con B y B coordina con C
    # Si ambas se cumplen, por transitividad también A coordina con C
    if len(A) == len(B) and len(B) == len(C):
        
        # Imprimimos la demostración paso a paso
        print("A coordina con B ✔")  # Confirmamos que A y B tienen la misma longitud
        print("B coordina con C ✔")  # Confirmamos que B y C tienen la misma longitud
        print("Por transitividad, A coordina con C ✔")  # Concluimos que A coordina con C
        
        # Mostramos las correspondencias explícitas entre A y C usando zip()
        # Esto empareja los elementos de A con los de C en orden
        print("Correspondencias A <-> C:", list(zip(A, C)))
    
    else:
        # Si la condición no se cumple, mostramos que la transitividad falla
        print("La transitividad no se cumple porque los conjuntos no tienen la misma longitud.")

# Ejemplo de uso:
# Definimos tres conjuntos distintos con la misma cantidad de elementos
A = [1, 2, 3]       # Conjunto A con números
B = ['a', 'b', 'c'] # Conjunto B con letras
C = ['x', 'y', 'z'] # Conjunto C con símbolos

# Llamamos a la función para verificar la transitividad entre A, B y C
verificar_transitividad(A, B, C)


    
    








































