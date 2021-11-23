import time

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            try: 
                if aux > max:
                    raise StopIteration
                n1 , n2 = n2 , aux
                counter += 1
                yield aux
            except StopIteration:
                break

if __name__ == '__main__':
    fibonacci = fibo_gen(21)
    for element in fibonacci:
        print(element)
        time.sleep(1)