mitupla=("Juan",13,1,1995)
miLista=["Ana",5,True,78.56]

milistaParse=list(mitupla)
mituplaParse=tuple(miLista)

print(mitupla[1])

print(mitupla)
print(milistaParse[:])
print(mituplaParse[:])

print(mitupla.count(13))#cuenta la apricion del elemento
print(len(mitupla))#logitud de la tupla


tupla=("Juan",)#Tupla unica
tupla1="Juan",13,48.55,True#Tupla empaquetada

nombre,dia,mes,agno=mitupla#Tupla desempaquetada
print(nombre)
print(dia)
print(agno)
print(mes)


