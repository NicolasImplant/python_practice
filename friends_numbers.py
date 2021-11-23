# Algoritmo para verificar si dos números son amigos:

def dividers(x: int, y:int) -> bool:
    div_x = [i for i in range(1, x) if x % i == 0]
    div_y = [i for i in range(1, y) if y % i == 0]
    return sum(div_x) == y and sum(div_y) == x

if __name__ == '__main__':
    nums = [None, None]

    for i in range(len(nums)):
        nums[i] = int(input("Escribe un número:    "))

print('Los números son amigos' if dividers(nums[0], nums[1]) else 'Los números NO son amigos')