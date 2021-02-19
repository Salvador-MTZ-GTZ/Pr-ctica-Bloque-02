Práctica Bloque 02:
Instrucciones
Formulas 3
LEE TODO ANTES DE COMENZAR ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← ←
Escribir un programa Python dentro una carpeta llamada “NoControl-PrácticaComplementaria-1”
dentro de esta carpeta crear un archivo llamado “generador_figuras2D.py”.
Se necesita tener en cuenta la siguiente funcionalidad, el programa deberá contener un menú dentro
de una función llamada main() el cual se ejecutará mientras el usuario lo desee, las opciones que
debe mostrar dicho menú son:
1.- Crear figura
2.- Listar una clasificación de figuras
3.- Listar todas las figuras
4.- Mostrar suma de todas las áreas
5.- Mostrar la suma de todos los perímetros
6.- Limpiar lista
0.- Salir
NOTA: Todas las figuras las almacenarás en una lista llamada, figuras (Será una lista de
diccionarios)
Opción 1
Esta deberá desplegar otro mené contenido dentro de una función llamada menu_figuras() el cual
debe contener las siguientes opciones:
NOTA: Los valores de las propiedades de cada figura deben ser proporcionados por el usuario.
1. Cuadrado
a. Al ser seleccionada deberás mandar a llamar una función nombrada
crear_cuadrado(lado) dentro de la cual crear un diccionario (Con la estructura que
muestro en la imagen de abajo).

2. Triángulo (Ojo: dentro de la función, basado en el valor de los argumentos debes determinar
si se trata de un triángulo equilátero, Isósceles o escaleno)
a. Al ser seleccionada deberás mandar a llamar una función nombrada
crear_triangulo(lado_a, lado_b, lado_c) dentro de la cual crear un diccionario (Con
la estructura que muestro en la imagen de abajo).

3. Círculo
a. Al ser seleccionada deberás mandar a llamar una función nombrada
crear_circulo(radio) dentro de la cual crearán un diccionario (Con la estructura que
muestro en la imagen de abajo).

Viernes 19 de Febrero 2021

El área y perímetro de cada figura se calcularán dentro de la función que crea la figura, pero estas
tendrán su función propia, es decir... la función crear_cuadrado(lado) llamará a la función
area_cudrado(lado) y a la función perimetro_cuadrado(lado) y el valor que retornan estas es lo
que almacenarás en el diccionario.
Finalmente agregarás el diccionario a la lista de figuras.

Opción 2
Se mandará a llamar una función listar_clasificacion(clasificacion) y según una palabra ingresada
por el usuario, el pedirá una clasificación de figuras (cuadrado, triángulo, círculo) para que se le
muestren todos los diccionarios registrados que tengan figuras de esa categoría.
NOTA: Si el usuario ingresa la categoría triángulo debes volver a preguntar y saber si quiere listar los
equiláteros, isósceles o escalenos.

NOTA: Deberás contemplar si el usuario ingresa opciones no válidas y desplegar un mensaje o
manejar el error de alguna manera.

NOTA: Si la clasificación que se quiere listar no tiene elementos en la lista debes notificarlo al usuario

Opción 3
Llamar una función imprimir() que muestre al usuario todas las figuras de la lista.
CHALLENGE: Esto NO es requisito, pero ponte a prueba Lista las figuras ordenadas según su
clasificación.
Opción 4
Mediante una función sumador_areas() muestra la suma total de todas las áreas POR
CLASIFICACIÓN de las figuras al usuario (AQUÍ NO ES NECESARIO QUE SEPARES LOS TIPOS
DE TRIÁNGULOS).
CHALLENGE: Esto NO es requisito, pero ponte a prueba separa por tipos de triángulos

Viernes 19 de Febrero 2021

Opción 5
Mediante una función sumador_perimetros() muestra la suma total de todos las perímetros POR
CLASIFICACIÓN de las figuras al usuario (AQUÍ NO ES NECESARIO QUE SEPARES LOS TIPOS
DE TRIÁNGULOS).
CHALLENGE: Esto NO es requisito, pero ponte a prueba separa por tipos de triángulos
Opción 5
Elimina a todos los elementos de la lista de figuras y notifica al usuario.
Opción 7 es decir... el 0
Termina la ejecución del programa

Formulas

Cuadrado
a = lado x lado
p = lado x 4
Círculo
a = π x radio2
p = 2 x π x radio
Triángulo equilátero (Los tres lados son iguales)

altura =

√3 x lado
2

area =
lado(base) x altura

2

perimetro = lado + lado + lado ó lado x 3

Triángulo isósceles (Tiene dos lados iguales y uno diferentes llamémoslos A y B donde A = C y B
representa el lado desigual
altura = √
A2− B2
4

area =
ladoB x altura
2

Viernes 19 de Febrero 2021

perimetro = A + B + C ó A + B x 2

Triángulo escaleno
sp = semi-perímetro

sp =
ladoA + ladoB + ladoC

2

area = √sp x (sp − ladoA) x (sp − ladoB) x (sp − ladoC)
Perimetro = ladoA + ladoB + ladoC
