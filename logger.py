from date_create import *

def create_contact():    
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    
    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def add_contact(contact):    
    with open('phonebook.txt', 'a', encoding='UTF-8' ) as file:
        file.write(contact)

def print_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        print(file.read().rstrip())
        for contact in enumerate(contacts_list, 1):
            print(*contact)

def search_contact():
    print(
        'Варианты поиска:\n'
        '1 - по фамилии\n'
        '2 - по имени\n'
        '3 - по отчеству\n'
        '4 - номеру телефона\n'
        '5 - по адресу\n'
    )
    
    var_search = input('Введите номер операции: ')
    
    while var_search  not in ('1', '2', '3', '4', '5'):
            print("Некорректный ввод данных! Попробуйте снова.")
            var_search = input('Выберите из представленного списка номер команды: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = contact_str.replace('/n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)

def copy_info():    
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        print(file.read().rstrip())
        
        for contact in enumerate(contacts_list, 1):
            print(*contact)

        select_number = int(input('Введите порядковый номер контакта для копирования в новый файл: '))       

        for index_num, contact in enumerate(contacts_list, 1):            
            if select_number == index_num:
                select_info = contact

    with open('copied_info.txt', 'a', encoding='UTF-8') as file:        
        file.write(f'{select_info}\n\n') 

    print (f"Скопированная информация: {select_info}")