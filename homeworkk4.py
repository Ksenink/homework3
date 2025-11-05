
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_owner_by_document_number(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None


print("Программа для работы с документами")
print("Доступные команды:")
print("p - найти владельца документа по номеру")
print("q - выход из программы")

while True:
    command = input("\nВведите команду: ").strip().lower()
    
    if command == 'q':
        print("Программа завершена.")
        break
    elif command == 'p':
        doc_number = input("Введите номер документа: ")
        owner = get_owner_by_document_number(doc_number)
        
        if owner:
            print(f"Владелец документа: {owner}")
        else:
            print("Документ с таким номером не найден")
    else:
        print("Неизвестная команда. Попробуйте снова.")