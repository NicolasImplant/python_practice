def primeNumber(number: int) -> bool:
    x = [1 for i in range(1,number+1) if number % i == 0]
    return len(x) == 2

def run():
    print(primeNumber(7))

if __name__ == '__main__':
    run()


