documents = [
    {'type': 'passport', 'number': '2207 876234', 'name':'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name':'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name':'Аристарх Павлов'},
]

directories = {
    '1':['2207 876234', '11-2'],
    '2':['10006'],
    '3':[]
}

# Задание 1 (Поиск имени владельца документа по его номеру)

def get_name_by_number():
    has_a_value = False
    doc_number=input('Введите номер документа')
    for i in documents:
        if i['number'] == doc_number:
            has_a_value = True
            print('Владелец документа:', i['name'])
            
    if has_a_value == False:
        print('Документ не найден в базе')
        
# Задание 2 (Поиск полки, на которой находтся документ по его номеру)

def get_directory():
    has_a_value = False
    doc_number = input('Введите номер документа')
    for i in documents:
        if i['number'] == doc_number:
            for key, value in directories.items():
                if doc_number in value:
                    has_a_value = True
                    print('Документ хранится на полке:', key)
    if has_a_value == False:
        print('Документ не найден в базе')
        

command = input('Введите команду:')
if command == 'p':
    get_name_by_number()
elif command == 's':
    get_directory()