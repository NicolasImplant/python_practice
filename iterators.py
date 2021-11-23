import time

class fiboIter():
    def __init__(self, max: int):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def __next__(self):
        if self.counter == 0:
            self.counter +=1
            return self.n1
        elif self.counter == 1:
            self.counter +=1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2 , self.aux
            self.counter +=1
            if not self.max or self.aux <= self.max:
                return self.aux
            else:
                raise StopIteration

if __name__ == "__main__":
    fibonacci = fiboIter(int(input('Escribe hasta donde quieres imprimir la secuencia de Fibonacci:  ')))
    for element in fibonacci:
        print(element)
        time.sleep(1)