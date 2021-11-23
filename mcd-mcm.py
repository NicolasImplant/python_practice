#Algoritmo para verificar el mínimo común divisor y el mínimo común multiplo

def mcd_mcm(x:int, y:int, z:float = 0) -> int:
    a , b = max(x,y), min(x,y)
    z = a % b
    if z != 0:
        return mcd_mcm(b,z)
    else:
        return b


if __name__ == '__main__':
    nums = [None, None]

    for i in range(len(nums)):
        nums[i] = int(input(f'{i+1}) Escribe un numero:  '))

print(f'El máximo común divisor es: {mcd_mcm(nums[0],nums[1])} y el mínimo común multiplo es: {(nums[0]*nums[1])/mcd_mcm(nums[0],nums[1])}')