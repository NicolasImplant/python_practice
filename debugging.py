def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]

def run():
    try:
        num = int(input('Ingresa el número:  '))
        if num == 0 or num < 0:
            raise ValueError
        print(divisors(num))
        print('Terminó mi programa =D')
    except ValueError:
        print("Debes ingresar un número entero positivo.")

if __name__ == '__main__':
    run()