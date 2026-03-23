'''
EJERCIO 1

Consigna
Se te proporciona un texto que contiene dos listas separadas por comas:

Una lista de personas: "Carlos,Juan,Pedro,Roque"

Una lista de sombreros: "Negro,Marron,Gris,Azul"

Tu tarea es escribir un programa en Python que:

Transforme cada lista en una estructura que puedas recorrer (usa split para convertirlas en listas).

Muestre la correspondencia perfecta entre cada persona y su sombrero usando indexación.

Ejemplo: Carlos ↔ Negro

Extraiga un subconjunto de la correspondencia usando slicing.

Muestra solo los dos primeros pares.

Descifra un mensaje secreto:

El mensaje está formado por las iniciales de cada persona y las iniciales de su sombrero.

Usa indexing para obtener la primera letra de cada nombre y sombrero.

Une esas letras en un string final y muéstralo como “Mensaje secreto”.
------------------------------------------------------------
Correspondencias:
Carlos ↔ Negro
Juan ↔ Marron
Pedro ↔ Gris
Roque ↔ Azul

Subconjunto:
Carlos ↔ Negro
Juan ↔ Marron

Mensaje secreto:
CNJMPRGA
==========================================================================================================================================================================

personas = "Carlos, Juan, Pedro, Roque"
sombreros = "Negro, Marron, Gris, Azul"
lista_personas = personas.split()
lista_sombreros = sombreros.split()
print (lista_personas)
print (lista_sombreros)
print ("Correspondencia:\n ",
       lista_personas[0], "<=>",lista_sombreros[0],"\n",
       lista_personas[1], "<=>",lista_sombreros[1],"\n",
       lista_personas[2], "<=>",lista_sombreros[2],"\n",
       lista_personas[3], "<=>",lista_sombreros[3]
       )
print("\nSubconjutno:")
sub_personas = lista_personas[0:2]
sub_sombreros = lista_sombreros [0:2]
print(sub_personas[0], "<=>", sub_sombreros[1])
print(sub_personas[1], "<=>", sub_sombreros[2])


mensaje = ""

for i in range (len(lista_personas)):
    mensaje += lista_personas[i][0] + lista_sombreros[i][0] # Mensaje = mensaje + lista_personas[i][0] + lista_sombreros[i][0]
print("Mensaje secreto:", mensaje)
============================================================================================================================================================================
'''
'''
EJERCICIO 2
Consigna
Se te proporciona un texto con dos listas:

"Matemáticas, Filosofía, Historia, Literatura"
"Estante1, Estante2, Estante3, Estante4"

Tu tarea es escribir un programa en Python que:

Transforme las listas en estructuras que puedas recorrer.
Muestre la correspondencia perfecta entre cada libro y su estante.

Extraiga un subconjunto de la correspondencia usando slicing.
Por ejemplo, mostrar solo los dos primeros pares.

Descifra un mensaje secreto:
El mensaje está formado por las iniciales de cada libro y las iniciales de su estante.
Usa indexing y stride para obtener las letras y formar el mensaje.

Niveles de abordaje sugeridos

Forma básica (conceptos básicos + nuevo):

Usa split para convertir los strings en listas.
Recorre las listas con un for y muestra la correspondencia.
Aplica slicing simple ([:2]) para mostrar un subconjunto.

Forma intermedia (conceptos intermedios + nuevo):

Usa indexación para obtener las iniciales de cada elemento.
Combina esas iniciales en un string.
Experimenta con stride ([::2]) para mostrar solo algunas letras del mensaje secreto.

Forma avanzada (conceptos avanzados + nuevo):
Crea funciones que reciban las listas y devuelvan la correspondencia.
Usa comprensión de listas para generar el mensaje secreto.
Integra slicing e indexación en una sola expresión.
'''

libros = "Matemáticas,Filosofía,Historia,Literatura,sociales,Armonia"   # Cadena con los nombres de los libros separados por comas
estantes = "Estante1,Estante2,Estante3,Estante4,estante5, estente6"    # Cadena con los nombres de los estantes separados por comas

lista_libros = libros.split(",")                                       # Convierte la cadena de libros en una lista, separando por comas
lista_estantes = estantes.split(",")                                   # Convierte la cadena de estantes en una lista, separando por comas
#HECHO POR LA IA
# -------------------------------
# FUNCIONES
# -------------------------------

# Correspondencia completa
print("Correspondencia completa:")
for libro, estante in zip(lista_libros, lista_estantes):   # zip recorre ambas listas en paralelo
    print(libro, "<->", estante)

# Subconjunto con slicing
print("\nPrimer subconjunto (0:2):")
for libro, estante in zip(lista_libros[:2], lista_estantes[:2]):  # slicing directo en ambas listas
    print(libro, "<->", estante)

print("\nSegundo subconjunto (2:4):")
for libro, estante in zip(lista_libros[2:4], lista_estantes[2:4]):
    print(libro, "<->", estante)

# Mensaje secreto
print("\nMensaje Secreto:")
# Comprensión de listas: toma inicial del libro y del estante en una sola expresión
iniciales = [libro[0] + estante[0] for libro, estante in zip(lista_libros, lista_estantes)]

# Une todas las iniciales en un string continuo
mensaje = "".join(iniciales)

# Aplica stride para filtrar (ejemplo: una de cada dos letras)
print("Mensaje completo:", mensaje)
print("Mensaje filtrado con stride:", mensaje[::2])



'''
print("Cantidad de libros:",len(lista_libros))                        # Muestra cuántos elementos tiene la lista de libros (en este caso 6)

print("Correspondencia entre libros y estantes: \n")
for i in range(len(lista_libros)):                                     # Recorre los índices desde 0 hasta la cantidad de libros - 1
    print(lista_libros[i], " <-> ", lista_estantes[i],)                 # Imprime el libro en la posición i junto con el estante en la misma posición

print("\n1er subconjunto par:\n") #LO HICE YO
for i in range(0,2):
    print(lista_libros[i], " <-> ", lista_estantes[i])

print("\n2do subconjunto par:\n") #ME AYUDO LA IA

sub_conjunto_libros = lista_libros[2:4]
sub_conjunto_estantes = lista_estantes[2:4]

for i in range(len(sub_conjunto_libros)):
    print(sub_conjunto_libros[i], "-", sub_conjunto_estantes[i])

print ("\nMensaje Secreto:\n")

for libros in lista_libros:
    print(libros[0], "-", libros[-1])
'''
































