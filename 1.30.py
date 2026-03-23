'''
Ejercicio:
“Coordinación de Pomos y Tapas”

Contexto matemático (Baldor)
Los postulados dicen que:

Si a dos conjuntos coordinables se les añade o quita un elemento, siguen siendo coordinables.
Dados dos conjuntos finitos, o son coordinables, o uno se coordina con parte del otro.
Si dos conjuntos están coordinados de cierta manera, siempre se puede coordinar de otra forma.
=====================================================================================================================
Consigna en Python
Imagina que tienes dos conjuntos representados como variables tipo string:

"Pomo1,Pomo2,Pomo3,Pomo4"

"Tapa1,Tapa2,Tapa3,Tapa4"

Tu tarea es:

Definir variables que contengan los conjuntos de pomos y tapas.
Mostrar la coordinación inicial entre cada pomo y su tapa.
Aplicar el primer postulado: añade un nuevo pomo y una nueva tapa como variables, y muestra la nueva coordinación.
Aplicar el segundo postulado: elimina un elemento de uno de los conjuntos y muestra cómo se coordina con parte del otro.
Aplicar el tercer postulado: cambia el orden de las tapas y muestra una nueva forma de coordinación.

Niveles de abordaje sugeridos

Forma básica (conceptos básicos + nuevo):

Declara variables simples con los strings.
Usa print para mostrar las correspondencias directamente.
Añade o elimina elementos escribiendo nuevas variables.
=============================================================================================================
Forma intermedia (conceptos intermedios + nuevo):

Convierte los strings en listas usando split.
Usa indexación para recorrer y mostrar correspondencias.
Aplica slicing para mostrar subconjuntos coordinados.
==============================================================================================================
Forma avanzada (conceptos avanzados + nuevo):

Crea funciones que reciban las listas y devuelvan la coordinación.
Usa comprensión de listas para generar las correspondencias.
Experimenta con stride para mostrar solo algunos pares (por ejemplo, cada segundo pomo con su tapa).
'''
'''
============================================================================
Forma básica (conceptos básicos + nuevo):

Declara variables simples con los strings.
Usa print para mostrar las correspondencias directamente.
Añade o elimina elementos escribiendo nuevas variables.

pomo1 = "pomo 1"
pomo2 = "pomo 2"
pomo3 = "pomo 3"
pomo4 = "pomo 4"
pomo5 = "pomo 5"
tapa1 = "tapa 1"
tapa2 = "tapa 2"
tapa3 = "tapa 3"
tapa4 = "tapa 4"
tapa5 = "tapa 5"
print ("Correspondencia:\n",
        
        pomo2, ">", tapa2,"\n",
        pomo3, ">", tapa3,"\n",
        pomo4, ">", tapa4,"\n",
        pomo4, ">", tapa4,"\n",
        pomo5, ">", tapa5,"\n",
       )
============================================================================
'''
'''
Forma intermedia (conceptos intermedios + nuevo):

Convierte los strings en listas usando split.
Usa indexación para recorrer y mostrar correspondencias.
Aplica slicing para mostrar subconjuntos coordinados.

pomos = "Pomo1,Pomo2,Pomo3,Pomo4"

tapas = "Tapa1,Tapa2,Tapa3,Tapa4"

lista_pomos = pomos.split(",")
lista_tapas = tapas.split(",")
print("\n",lista_pomos[0],"->",lista_tapas[0],"\n",
      lista_pomos[1],"->",lista_tapas[1],"\n",
      lista_pomos[2],"->",lista_tapas[2],"\n",
      lista_pomos[3],"->",lista_tapas[3],"\n",
      )

print ("Subconjuntos coordinados: ","\n",
      lista_pomos[0:1],"->",lista_tapas[0:1],"\n",
      lista_pomos[1:2],"->",lista_tapas[1:2],"\n",
      lista_pomos[2:3],"->",lista_tapas[2:3],"\n",
      lista_pomos[3:4],"->",lista_tapas[3:4],"\n",)
=================================================================================
'''

'''
Forma avanzada (conceptos avanzados + nuevo):

Crea funciones que reciban las listas y devuelvan la coordinación.
Usa comprensión de listas para generar las correspondencias.
Experimenta con stride para mostrar solo algunos pares (por ejemplo, cada segundo pomo con su tapa).

def recibir_listas(pomos, tapas):
    lista_pomos = pomos.split(",")
    lista_tapas = tapas.split(",")
    par_subconjunto = lista_pomos[0],">", lista_tapas[1]

    return lista_pomos, lista_tapas, par_subconjunto

pomos,tapas,par_subconjunto = recibir_listas("pomo1, pomo2, pomo3", "tapa1, tapa2, tapa3")


print("\n",pomos,"\n",tapas,"\n",par_subconjunto)
=====================================================================================
'''
#EJEMPLOS DE LA IA Y CORREGIDOS

'''
=============
FORMA BASICA:
=============
# Declarar variables simples con strings
pomos = "Pomo1,Pomo2,Pomo3,Pomo4"
tapas = "Tapa1,Tapa2,Tapa3,Tapa4"

print("Coordinación inicial:")
print("Pomo1 -> Tapa1")
print("Pomo2 -> Tapa2")
print("Pomo3 -> Tapa3")
print("Pomo4 -> Tapa4")

# Postulado 1: añadir un nuevo pomo y tapa
pomos = "Pomo1,Pomo2,Pomo3,Pomo4,Pomo5"
tapas = "Tapa1,Tapa2,Tapa3,Tapa4,Tapa5"
print("\nNueva coordinación con elementos añadidos:")
print("Pomo5 -> Tapa5")

# Postulado 2: eliminar un elemento de tapas
tapas = "Tapa1,Tapa2,Tapa3"
print("\nCoordinación parcial (pomos con parte de tapas):")
print("Pomo1 -> Tapa1")
print("Pomo2 -> Tapa2")
print("Pomo3 -> Tapa3")

# Postulado 3: cambiar el orden de tapas
tapas = "Tapa3,Tapa1,Tapa2"
print("\nNueva forma de coordinación:")
print("Pomo1 -> Tapa3")
print("Pomo2 -> Tapa1")
print("Pomo3 -> Tapa2")
'''
'''
=================
fORMA INTERMEDIA
=================
# Convertir strings en listas
pomos = "Pomo1,Pomo2,Pomo3,Pomo4"
tapas = "Tapa1,Tapa2,Tapa3,Tapa4"

lista_pomos = pomos.split(",")
lista_tapas = tapas.split(",")

print("Coordinación inicial:")
for i in range(len(lista_pomos)):
    print(lista_pomos[i], "->", lista_tapas[i])

# Postulado 1: añadir elementos
lista_pomos.append("Pomo5")
lista_tapas.append("Tapa5")
print("\nNueva coordinación con elementos añadidos:")
print(lista_pomos[-1], "->", lista_tapas[-1])

# Postulado 2: eliminar un elemento de tapas
lista_tapas.pop()  # quitamos la última tapa
print("\nCoordinación parcial:")
for i in range(len(lista_tapas)):
    print(lista_pomos[i], "->", lista_tapas[i])

# Postulado 3: cambiar el orden de tapas
lista_tapas = lista_tapas[::-1]  # invertir orden
print("\nNueva forma de coordinación:")
for i in range(len(lista_tapas)):
    print(lista_pomos[i], "->", lista_tapas[i])
'''

'''
===============
FORMA AVANZADA
===============
def recibir_listas(pomos, tapas):
    lista_pomos = [p.strip() for p in pomos.split(",")]
    lista_tapas = [t.strip() for t in tapas.split(",")]
    return lista_pomos, lista_tapas

def mostrar_coordinacion(lista_pomos, lista_tapas):
    return [f"{p} -> {t}" for p, t in zip(lista_pomos, lista_tapas)]

# Coordinación inicial
pomos, tapas = recibir_listas("Pomo1,Pomo2,Pomo3,Pomo4", "Tapa1,Tapa2,Tapa3,Tapa4")
print("Coordinación inicial:")
print("\n".join(mostrar_coordinacion(pomos, tapas)))

# Postulado 1: añadir elementos
pomos.append("Pomo5")
tapas.append("Tapa5")
print("\nNueva coordinación con elementos añadidos:")
print("\n".join(mostrar_coordinacion(pomos, tapas)))

# Postulado 2: eliminar un elemento de tapas
tapas.pop()
print("\nCoordinación parcial:")
print("\n".join(mostrar_coordinacion(pomos, tapas)))

# Postulado 3: cambiar el orden de tapas
tapas = tapas[::-1]
print("\nNueva forma de coordinación:")
print("\n".join(mostrar_coordinacion(pomos, tapas)))

# Extra: stride (cada segundo pomo con su tapa)
print("\nCoordinación alterna (stride):")
print("\n".join(mostrar_coordinacion(pomos[::2], tapas[::2])))
'''







































