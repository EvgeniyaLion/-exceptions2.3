documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

def get_people(documents):
    doc_number = input('Введите номер документа:')
    for document in documents:
      if doc_number in document.values():
        print(document['name'])
        return
    print('Документа с таким номером не существует')

def get_list(documents):
    if bool(documents):
      for doc_list in documents:
        print(f'''{doc_list['type']} \'{doc_list['number']}\' \'{doc_list['name']}\'''')
    else:
      print('Нет ни одного документа')

def get_shelf(directories):
    doc_number = input('Введите номер документа:')
    for number, shelf in directories.items():
      if doc_number in shelf:
        print(f'Документ хранится на полке №{number}')
        return
    print('Документа с таким номером не существует')

def add_doc():
    new_doc={}
    
    print('Введите номер документа:')
    doc_number = input()
    print('Введите тип документа:')
    doc_type = input()
    print('Введите имя владельца документа:')
    doc_name = input()
    print('Введите номер полки для хранения:')
    shelf_number = input()

    new_doc.update({"type": doc_type, "number": doc_number, "name": doc_name})
    documents.append(new_doc)

    if shelf_number in directories.keys():
        directories[shelf_number].append(doc_number)
    else:
        directories[shelf_number] = [doc_number]

    print(f'Документ {new_doc} добавлен на полку {shelf_number}')

def delete_doc(doc_number):
    doc_number = input('Введите номер документа:')
    for document in documents:
        if doc_number in document.values():
            for number, directory in directories.items():
                if doc_number in directory:
                    directories[number].remove(doc_number)
                    documents.remove(document)
                    print(f'Документ с номером {doc_number} удален')
                    return
    print('Документа с таким номером не существует')

def move_doc(doc_number):
    doc_number = input('Введите номер документа:')
    variable = False
    old_shelf_number = '1'
    for number, directory in directories.items():
        if doc_number in directory:
            variable = True
            old_shelf_number = number
            break
    if not variable:
        print('Документа с таким номером не существует')
        return
    new_shelf_number = input('Введите новый № полки:')
    if new_shelf_number in directories.keys():
        directories[old_shelf_number].remove(doc_number)
        directories[new_shelf_number].append(doc_number)
    else:
        directories[new_shelf_number] = [doc_number]
    print(f'Документ {doc_number} успешно перемещен на полку {new_shelf_number}')


def add_shelf(shelf_number):
    shelf_number = input('Введите номер полки, которую хотите добавить:')
    if shelf_number in directories.keys():
        print('Полка с таким номером уже существует')
        return
    directories[shelf_number] = []
    print(f'Полка № {shelf_number} добавлена')

def no_name(documents):
    for doc in documents:
        try:
            print(doc['name'])
        except KeyError:
            print(f'Документ {doc["number"]} не имеет имени владельца')

def main():
    while True:
      print('Введите\n n, чтобы посмотреть имена владельцев документов;\n p, чтобы найти имя владельца по номеру документа;\n l, чтобы посмотреть список всех документов;\n s, чтобы по номеру документа узнать полку, на которой он находится;\n a, чтобы добавить новый документ в каталог и в перечень полок;\n d, чтобы удалить документ из каталога и из перечня полок;\n m, чтобы переместить документ с одной полки на другую;\n as, чтобы добавить новую полку в перечень;\n q, чтобы выйти')
      user_input = input()
      if user_input == 'p':
        get_people(documents)
      elif user_input == 'l':
        get_list(documents)
      elif user_input == 's':
        get_shelf(directories)
      elif user_input == 'a':
        add_doc()
      elif user_input == 'd':
        delete_doc(documents)
      elif user_input == 'm':
        move_doc(documents)
      elif user_input == 'as':
        add_shelf(directories)
      elif user_input == 'n':
        no_name(documents)
      elif user_input == 'q':
        break
      else:
        print('Некорректный ввод')

main()
