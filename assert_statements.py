def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]

def run():
    num = input('Ingresa el número:  ')
    assert num.isnumeric() and int(num) > 0, 'Debes ingresar un número entero positivo'
    print(divisors(int(num)))
    print('Terminó mi programa =D')

if __name__ == '__main__':
    run()