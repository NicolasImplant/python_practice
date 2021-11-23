#función para realizar la descomposición en factores primos de un número ingresado por el usuario.

def factors(n:int, fact:list = []) -> list:
    x = {n: [i for i in range(1, n+1) if n % i == 0] for n in range(1,1000)}
    for key, value in x.items():
        if len(value) == 2:
            fact.append(key)
    def descomposition(n: int, fact: list, fact1: list = []) -> list:
        for k in fact:
            while n % k == 0:
                n /= k
                fact1.append(k)
        return fact1    
    return descomposition(n,fact)


if __name__ == '__main__':
    n = int(input('Escribe un número:  '))
    print(f'El número {n} es el producto de los siguientes números primos: {factors(n)}')