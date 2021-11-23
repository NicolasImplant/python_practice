def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"First_name": "Nicolás", "Last_name": "Patiño"}
    
    super_list = [
        {"First_name": "Nicolás", "Last_name": "Patiño"},
        {"First_name": "Diego", "Last_name": "Rodríguez"},
        {"First_name": "Isabella", "Last_name": "Patiño"},
        {"First_name": "Ana Maria", "Last_name": "Rodríguez"},
        {"First_name": "Nathalia", "Last_name": "Morales"}
    ]
    super_dict = {
        "Natural_nums" : [1, 2, 3, 4, 5],
        "Integer_nums" : [-2, -1, 0, 1, 2],
        "Floating_nums": [1.1, 1.2, 1.3, 1.4, 1.5]
        }
    
    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)

if __name__ == "__main__":
    run()