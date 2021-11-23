from decoradores import random_func


my_set1 = {1,2,3,4,5,'Hola'}
my_set2 = {5,6,7,8,9,10,'Hola'}

print(f'Los sets de prueba son: {my_set1} y {my_set2}')
#Agregar  un elemento al set
my_set1.add(9)
print(my_set1)

# Agregar varios elementos al set

my_set2.update([3,5,6])
print(my_set2)

#Elimina un elemento existente dentro del set si el elemento no existe en el set se genera error
my_set2.remove('Hola')
my_set1.remove(9)
print(my_set2)
print(my_set1)

# Elimina un elemento del set, en caso de que el elemento en mencion no sea parte del set, deja inmutado el mismo

my_set1.discard(20)
print(my_set1)

#Elimina un elemento del set de manera aleatoria
my_set2.pop()
print(my_set2)

#Eliminar todos los elementos del set

# my_set1.clear()
# print(my_set1)

# Unir los dos sets
my_set3 = my_set1 | my_set2
my_set3b = my_set1.union(my_set2) 

print(my_set3, my_set3b)

# interceptar los dos sets

my_set4 = my_set1 & my_set2
my_set4b = my_set1.intersection(my_set2)

print(my_set4, my_set4b)

# Diferencia entre los sets

my_set5 = my_set1 - my_set2
my_set5b = my_set1.difference(my_set2)

print(my_set5, my_set5b)

# Diferencia simetrica

my_set6 = my_set1 ^ my_set2
my_set6b = my_set1.symmetric_difference(my_set2)
print(my_set6, my_set6b)

# Eliminando los valores repetidos de una lista

# [1,1,1,2,3,4,4] -> [1,2,3,4]
 
def remove_duplicates(some_list: list) -> list:
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1,1,1,2,3,4,4]
    print(remove_duplicates(random_list))

def reto():
    random_list = [1,1,1,2,3,4,4]
    return set(random_list)

if __name__ == '__main__':
    run()
    print(reto())