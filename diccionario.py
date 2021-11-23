def run():
    dictionary = {}
    for i in range(1,101):
        if i % 3 != 0:
            dictionary[i] = i**3        
    print(dictionary)

    dictionary = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(dictionary)

    dic = {i : round(i**(1/2),2) for i in range(1,1001)}
    print(dic)

if __name__ == '__main__':
    run()