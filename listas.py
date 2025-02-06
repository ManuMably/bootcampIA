# lista con 5 numeros enteros, 1. ordenar de menor a mayor, 2. segundo numero mas grande de la lista, 3. calcular promedio de la lista
lista = [2,1,5,4,3]
#1 el metodo sort ordena de menor a mayor
lista.sort()
print(lista)
#2 segundo numero mas grande de la lista
primeroMayor = max(lista)
print(primeroMayor)
lista.remove(primeroMayor)
segundoMayor = max(lista)
print("el segundo numero mas grande es",segundoMayor)
#3 promedio de la lista
suma = 0
for x in lista:
    suma = suma + x
promedio = suma / len(lista)
print("el promedio de la lista es", promedio)

# lista con 5 palabras
palabras = ["perro","gato","tortuga","medusa","tiburon"]
print("la cantidad de palabras en la lista son: ", len(palabras))
print("la palabra mas larga es: ", max(palabras))
print("la palabra mas corta es: ", min(palabras))
print(" ".join(palabras))