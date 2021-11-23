def run():
    nums = []
    for i in range(1,101):
         if i**2 % 3 != 0:
             nums.append(i**2)
    print(nums)

    squares = [i for i in range(100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squares)

    list = [1,2,3,4,5]
    squares = [i**2 for i in list]
    print(squares)

if __name__=='__main__':
    run()

