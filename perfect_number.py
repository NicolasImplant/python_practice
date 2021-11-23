#Algoritmo para verificar si un número es perfecto

def perfect(x:int, i:int = 2, z:int = 0) -> int or bool:
    while z != x:
        z = (2**(i-1))*((2**i)-1)
        i+=1
        if z > x:
            break
            return False
    return z

if __name__ == '__main__':
    n = int(input("Digita un número:  "))
    print('Es un numero perfecto ' if n == perfect(n) else 'No es un numero perfecto')