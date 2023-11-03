def file_read():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        return file.read()


def file_append(text=""):
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(text)


def input_data():
    sur = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    pat = input("Введите Отчество: ")
    phone = input("Введите Телефон: ")
    adr = input("Введите Адрес: ")

    contact_str = f"{sur} {name} {pat} {phone} {adr}\n" 
    file_append(contact_str)
    #print(contact_str)

def print_data():
    print(file_read())

def search_contact():
    print("Возможные варианты поиска:\n"
         "1. По фамилии\n"
         "2. По имени\n"
         "3. По отчеству\n"
         "4. По номеру телефона\n"
         "5. По адресу\n")    
    command = input("Выберите вариант поиска: ")

    while command not in ("1","2","3","4","5"):        
        print("Некорректный ввод, повторите попытку")
        command = input("Выберите вариант поиска: ")
    
    i_var = int(command) - 1

    search = input("Введите данные для поиска: ")
    print()
    contacts_list = file_read().rstrip().split("\n")
    print("contacts_list", contacts_list)

    for contact_str in contacts_list:
        cont_list = contact_str.replace("\n","").split()
        if search in cont_list[i_var]:
            return contact_str

def change_contact():
    find_cont: str = search_contact()
    # print(find_cont)
    find_str = "".join(find_cont)
    find_arr = find_cont.split()
    # print('find_arr', find_str)

    enter = int(input("Что хотите изменить?: \n"
        "1. Фамилию\n"
        "2. Имя\n"
        "3. Отчество\n"
        "4. Номер телефона\n"
        "5. Адрес\n")) - 1
    new_mean = input ("Введите новое значение: ")    
    find_arr[enter] = new_mean
    test = ' '.join(find_arr)
    print('test', test)

    with open("phonebook.txt", "r", encoding="UTF-8") as file: 
        data = file.readlines()
        # print('data', data)
    with open("phonebook.txt", "w+") as file:
        for line in data:
            if not line.isspace():
                line = line.rstrip()
                print('line', line)
                if line == find_cont:
                    file.write(f"{test}\n") 
                else:
                    file.write(f"{line}\n")      


def delete_contact():
    find_cont: str = search_contact()
    # print("find ", find_cont, "***")
    with open("phonebook.txt", "r", encoding="UTF-8") as file: 
        data = file.readlines()
        # print("fileread data", data)
    with open("phonebook.txt", "w+") as file:
        for line in data:
            line = line.strip()
            if line != find_cont:
                file.write(f"{line}\n")

        # print('data', data)

def u_interface():
    command = ""
    while command != "6":
        print("Меню:\n"
            "1. Добавить контакт\n"
            "2. Найти контакт\n"
            "3. Вывести все контакты\n"
            "4. Изменить контакт\n"
            "5. Удалить контакт\n"
            "6. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1","2","3","4","5","6"):        
            print("Некорректный ввод, повторите попытку")
            command = input("Выберите пункт меню: ")

        print()        
        match command:            
            case "1":
                input_data()
            case "2":
                print(search_contact())
            case "3":
                print_data()
            case "4":
                change_contact()
            case "5":
                delete_contact()
            case "6":
                print("Всего хорошего!")

u_interface()