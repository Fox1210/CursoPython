miLista=["Ana",5,True,78.56]
miLista2=["Sandra","Lucia"]

miLista3=miLista+miLista2#Une dos listas
print(miLista3[:])

miLista2=miLista2*2#repite 2 veces el contenido de la lista
print(miLista2[:])

#Añadir a lista
miLista.append("Roberto")#Añade al final
print(miLista[:])
miLista.insert(2,"Lola")#Añade en un indice
print(miLista[:])
miLista.extend([True,"Alaba","Ana","Pepe","Luis"])#Concatena una Lista a otra
print(miLista[:])

#Borrar de una lista
miLista.remove(True)#Borra el primer elemeto que encuentra
print(miLista[:])
miLista.pop()#Borra el ultumo elemento añadido
print(miLista[:])


#Funciones de las listas
print(miLista.index("Pepe"))#Indica el indice de Pepe en la lista
print(miLista.index("Ana"))#Indica el primer elemento

print("Pepe" in miLista)# devuelve true si existe en la lista y flase si no existe

#Indices de listas
print(miLista[2])
print(miLista[-2])
#Poriones de listas
print(miLista[0:2])#Ana, 5 -- NO MARTA
print(miLista[:2])#Ana, 5 -- NO MARTA
print(miLista[1:2])#5 -- NO MARTA

print(miLista[2:])#Muestra desde el indice 2 hasta el final