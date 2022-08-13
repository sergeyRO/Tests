documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }

# 1Поиск владельца по номеру документа
def search_people(number_doc):
    for doc in documents:
        if doc['number'] == number_doc:
            return doc['name']

# 2Поиск документа на полке
def search_shelf(number_doc):
    for key, docs in directories.items():
        if number_doc in docs:
            return key
    return 0

# 3Список всех документов
def search_list():
    for doc in documents:
        print(f"{doc['type']} \"{doc['number']}\" \"{doc['name']}\"")
    return documents

# 4Добавление документа
def add_doc(number_doc, type_doc, owner, shelf):
    val = directories.get(shelf, None)
    if val != None:
        documents.append(dict(type=type_doc, number=number_doc, name=owner))
        val.append(number_doc)
        directories[shelf] = val
        print(f"Документ добавлен в список и на полку {shelf}")
        return True
    else:
        print("Полка {shelf} отсутствует! Документ не добавлен!")
        return False

# Удаление документа
def drop_doc(number_doc):
    document = False
    directory = False
    for doc in documents:
        if doc['number'] == number_doc:
            documents.remove(doc)
            document = True
            break
    for key, docs in directories.items():
        if number_doc in docs:
            docs.remove(number_doc)
            directory = True
            break
    if document and directory:
        print("Документ удалён из списков и с полки")
        return True
    else:
        if document and not directory:
            print("Документ отсутствует на полке, но удалён из списка")
        elif not document and directory:
            print("Документ отсутствует в списке, но удалён с полки")
        else:
            print("Документ не существует")
        return False

# Перемещение документа
def modify_doc(number_doc, shelf):
    document = False
    if shelf in directories:
        for key, docs in directories.items():
            if number_doc in docs:
                docs.remove(number_doc)
                document = True
                directories[shelf].append(number_doc)
                break
        if not document:
            print(f"Документ {number_doc} не существует!")
            return False
        else:
            print(f"Документ {number_doc} перенесён на полку {shelf}")
            return True
    else:
        print(f"Полка {shelf} не существует!")
        return False

# Добавить полку
def add_shelf(shelf):
    if shelf in directories:
        print(f"Полка {shelf} существует!")
        return False
    else:
        directories.setdefault(shelf, [])
        print(f"Полка {shelf} добавлена!")
        return True

# Выход из программы
def command_exit():
    res = "EXIT"
    return res

if __name__ == '__main__':

    # Ввод
    while True:
        command = input("Введите команду: ")
        if command == "p":
            number_doc = input("Введите номер документа: ")
            print(search_people(number_doc))
        elif command == "s":
            number_doc = input("Введите номер документа: ")
            key = search_shelf(number_doc)
            if key != 0:
                print(f"Документ находится на полке {key}")
            else:
                print(f"Данный документ отсутствует!")
        elif command == "l":
            search_list()
        elif command == "a":
            number_doc = input("Введите номер документа: ")
            type_doc = input("Введите тип документа: ")
            owner = input("Введите владельца: ")
            shelf = input("Введите номер полки для хранения: ")
            print(add_doc(number_doc, type_doc, owner, shelf))
            print(directories)
        elif command == "d":
            number_doc = input("Введите номер документа: ")
            print(drop_doc(number_doc))
            print(directories)
            print(documents)
        elif command == "m":
            number_doc = input("Введите номер документа: ")
            shelf = input("Введите номер полки для хранения: ")
            print(modify_doc(number_doc, shelf))
            print(directories)
        elif command == "as":
            shelf = input("Введите номер полки для хранения: ")
            print(add_shelf(shelf))
            print(directories)
        elif command == "q":
            print(command_exit())
            quit()
        else:
            print("Несуществующая команда!")