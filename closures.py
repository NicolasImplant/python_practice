#Hola 3 -> HolaHolaHola

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas type String"
        return string * n
    return repeater

def make_division(x):
    def division(n):
        assert type(n) == int, 'Debes ingresar números'
        assert type(x) == int, 'Debes ingresar números'
        return int(x/n)
    return division

def run():
    repeat_5 = make_repeater_of(3)
    repeat_2 = make_repeater_of(2)
    repeat_4 = make_repeater_of(4)
    print(repeat_5('Hola'))
    print(repeat_2('Nicolás'))
    print(repeat_4('Platzi'))

    div1 = make_division(20)
    print(div1(20))

if __name__ == '__main__':
    run()