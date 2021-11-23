def factorial(n:int, memo:dict={}) -> int:
    if n == 0:
        return 1
    try:
        return memo[n]
    except KeyError:
        memo[n] = n * factorial(n-1, memo)
        return memo[n]

if __name__ == '__main__':
    N     = int(input('Cuantas iteraciones quieres que realize la serie?:  '))
    num   = int(input('Que deseas calcular?  1 = Euler, 2 = Sen(x):  '))
    sen_x = [0, None]
    e     = 0
    if num == 2:
        sen_x[1] = int(input('Escribe el argumento de la función seno:  '))
    
    for i in range(N):
        if num == 1:
            e += 1/factorial(i)
        else:
            sen_x[0] += ((-1)**i)*(sen_x[1]**((2*i)+1))/factorial((2*i)+1)
            

print(e,sen_x[0])