arcoiris=("azul","verde","rojo","amarillo")
print(arcoiris)
print("-LONGITUD ARCOIRIS--")
print(len(arcoiris))
animales=("pantera",20,"estatura",1.7)
print(animales)
print("ELEMENTOS DE LA TUPLA")
print(animales[0])
ratero = ("juan", "ana", "pedro")
y = list(ratero)
y[1] = "bolainas"
x = tuple(y)
print(x)
print("agregando elementos")
Nanimal=("bobby","chetos")
y = list(Nanimal)
print(y)
y.append("tontolin")
otratupla = tuple(y)
print(otratupla)
print("USO DE FOR EN TUPLAS")
for elcolor in arcoiris:
    print(elcolor)
    