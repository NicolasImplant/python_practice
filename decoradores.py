from datetime import datetime

def mayusculas(func):
    def envoltura(texto):
        assert type(texto) == str, 'Debes ingresar un String'
        return func(texto).upper()
    return envoltura

@mayusculas
def saludo(texto):
    return f'Hola {texto} este es un decorador'

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' Segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo2(nombre = 'Nicolás'):
    print(f'Hola {nombre} son las: {datetime.now()}')


@execution_time
def cicloUno(n = 1000000):
    for _ in range(1,n):
        pass

if __name__ == '__main__':
    n = 10
    for _ in range(10):
        cicloUno(n)
        n*=100