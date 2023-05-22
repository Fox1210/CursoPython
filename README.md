# Python
En este documento se redactan las notas del [curso Pyhrton desde cero](https://youtube.com/playlist?list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS)

*By Pablo Gómez Meléndez*

## Introducción

Python es un lenguaje de **muy alto nivel**, es decir el lenguaje de programación que se asemeja mucho al lenguje común. Además posee una gramatica **simple, clara y muy ligera**. Es un lenguaje con **tipado dinamico y fuerte**, el tipo de dato se asina de forma dinamica, en tiempo de ejecución. Tambien es un lenguaje que permite el **POO**: sobrecarga de constructores, __*herencia múltiple*__, encapsulación, interfaces y polimorfismo. Es un lenguaje **multiplataforma**.

## Sintaxis básica

La **intrucción** es una linea de código que realiza una acción, no termina con ";".

Los **comentarios** en Python se pones usando en *#* la linea a comentar.

Para añadir un salto de línea se utiliza la " \ ", un ejemplo de esto seria:

```python
mi_nombre="mi nombre es 
Pablo"
```
### Funciones

Las funciones de declaran con el siguinete termino:

```python
def nombre_funcion():
    Instruciones de la funcion
    return(opcional)

 def nombre_funcion(paremetros): 
    Instruciones de la funcion 
    return(opcional)
```

Las funciones se llaman directamnte por el nombre y si es necesrio se pasan los parmaetros

```python
nombre_funcion()
nombre_funcion(paremetros)
```
### Listas
Las listas en este lenguaje son **dinamicas**  y además tienen la peculiaridad de poder guardar **distintos** tipos de datos

```python
nombreLista=[elem0,elem1,elem2,elem3,elem4,...]
```
### Tuplas
Las tuplas son listas **INMUTABLES**, es decir, no permite su modificacion despues de su creación
- Permiten extraer porciones, pero el resultado es una nueva tupla
- No permite la busqueda por indice
- Perimite comprobar si un elemento exite en la tupla
Las ventajas que tiene la tupla respiecto a las listas son:
- Más rápidas
- Menos espacio(mayor optimización)
- Formatean los string
- Pueden Utilizarse como clasves para diccionarios

```python
nombreLista=(elem0,elem1,elem2,elem3,elem4,...)
```