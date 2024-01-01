# # Создать телефонный справочник с возможностью импорта и экспорта данных 
# # в формате .txt. Фамилия, имя, отчество, номер телефона - данные, 
# # которые должны находиться в файле.  Программа должна выводить данные
# # Программа должна сохранять данные в текстовом файле
# # Пользователь может ввести одну из характеристик для поиска определенной 
# # записи(Например имя или фамилию человека)
# # Использование функций. Ваша программа не должна быть линейной

# # Этапы работы:
# # 1) Создать телефонный справочник:                                         +
# #     - открыть файл в режиме "a" ;                                         +
# # 2) Добавить контакт:                                                      +
# #     - запросить у пользователя информацию;                                +
# #     - подготовить данные под необходимый формат для записи информации;    +
# #     - открыть файл для записи в режиме "a";                               +
# #     - добавить информацию в файл;                                         +
# # 3) Вывести данные из файла на экран:                                      +
# #     - открыть файл в режиме чтения "r";                                   +
# #     - вывести информации на экран;                                        +
# # 4) Поиск данных:                                                          +
# #     - запросить вариант поиска;                                           
# #     - запросить информацию для поиска у пользователя;                     +
# #     - открыть файл в режиме чтения "r";                                   +
# #     - сохранить данные в переменную                                       +
# #     - осуществить поиск по файлу;                                         +
# #     - вывести нужную информацию на экран;                                 +
# # 5) Реализовать UI:                                                        +
# #     - вывести варианты меню;                                              +
# #     - получение запроса пользователя;                                     +
# #     - реализация запроса пользователя;                                    +
# #     - выход из программы;                                                 +

# def input_name():
#     return input('Введите имя: ')

# def input_surname():
#     return input('Введите фамилию: ')

# def input_patronymic():    
#     return input('Введите отчество: ')

# def input_phone():
#     return input('Введите телефон: ')

# def input_address():
#     return input ('Введите адресс: ')

# def create_contact():    
#     surname = input_surname()
#     name = input_name()
#     patronymic = input_patronymic()
#     phone = input_phone()
#     address = input_address()
    
#     return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

# def add_contact(contact):    
#     with open('phonebook.txt', 'a', encoding='UTF-8' ) as file:
#         file.write(contact)

# def print_info():
#     with open('phonebook.txt', 'r', encoding='UTF-8') as file:
#         contacts_list = file.read().rstrip().split('\n\n')
#         print(file.read().rstrip())
#         for contact in enumerate(contacts_list, 1):
#             print(*contact)

# def search_contact():
#     print(
#         'Варианты поиска:\n'
#         '1 - по фамилии\n'
#         '2 - по имени\n'
#         '3 - по отчеству\n'
#         '4 - номеру телефона\n'
#         '5 - по адресу\n'
#     )
    
#     var_search = input('Введите номер операции: ')
    
#     while var_search  not in ('1', '2', '3', '4', '5'):
#             print("Некорректный ввод данных! Попробуйте снова.")
#             var_search = input('Выберите из представленного списка номер команды: ')

#     index_var = int(var_search) - 1

#     search = input('Введите данные для поиска: ')

#     with open('phonebook.txt', 'r', encoding='UTF-8') as file:
#         contacts_list = file.read().rstrip().split('\n\n')

#     for contact_str in contacts_list:
#         contact_lst = contact_str.replace('/n', ' ').split()
#         if search in contact_lst[index_var]:
#             print(contact_str)

# def interface():
#     with open('phonebook.txt', 'a', encoding='UTF-8'):
#         pass  

#     command = '-1'

#     while command != '4':
#         print('Доступные запросы: \n'
#                 '1. Добавить контакт.\n'
#                 '2. Вывести на экран\n'
#                 '3. Поиск контакта\n'
#                 '4. Выход из программы')

#         command = input('Выберите из представленного списка номер команды: ')

#         while command  not in ('1', '2', '3', '4'):
#             print("Некорректный ввод данных! Введите ")
#             command = input('Выберите из представленного списка номер команды: ')

#         match command:
#             case '1':
#                 add_contact(create_contact())
#             case '2':
#                 print_info()
#             case '3':
#                 search_contact()
#             case '4':
#                 print('Good bye!')
    
# interface()