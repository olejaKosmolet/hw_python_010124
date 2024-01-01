from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass  

    command = '-1'

    while command != '5':
        print('Доступные запросы: \n'
                '1. Добавить контакт.\n'
                '2. Вывести на экран\n'
                '3. Поиск контакта\n'
                '4. Копировать контакт\n'
                '5. Выход из программы')

        command = input('Выберите из представленного списка номер команды: ')

        while command not in ('1', '2', '3', '4', '5'):
            print("Некорректный ввод данных! Введите ")
            command = input('Выберите из представленного списка номер команды: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                print_info()
            case '3':
                search_contact()
            case '4':
                copy_info()
            case '5':
                print('До свидания!')