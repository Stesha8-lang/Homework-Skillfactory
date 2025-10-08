import random

# Начальные данные
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']

# Генерация оценок
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]
        students_marks[student][class_] = marks

# Меню команд
def print_menu():
    print('''
Список команд:
1. Добавить оценку ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить оценку
5. Редактировать оценку
6. Добавить нового ученика
7. Удалить ученика
8. Добавить новый предмет
9. Удалить предмет
10. Показать все оценки конкретного ученика
11. Показать средний балл по каждому предмету для конкретного ученика
12. Выход
''')

while True:
    print_menu()
    try:
        command = int(input('Введите команду: '))
    except ValueError:
        print("Ошибка: введите число.")
        continue

    if command == 1:
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        try:
            mark = int(input('Введите оценку: '))
        except ValueError:
            print("Ошибка: введите число.")
            continue
        if student in students_marks and class_ in students_marks[student]:
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('Ошибка: неверное имя ученика или предмет.')

    elif command == 2:
        for student in students:
            print(student)
            for class_ in classes:
                marks = students_marks[student][class_]
                avg = sum(marks) / len(marks)
                print(f'{class_} - {avg:.2f}')
            print()

    elif command == 3:
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:  # Удалить оценку
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f'Оценки: {students_marks[student][class_]}')
            try:
                index = int(input('Введите индекс оценки для удаления (начиная с 0): '))
                if 0 <= index < len(students_marks[student][class_]):
                    removed = students_marks[student][class_].pop(index)
                    print(f'Удалена оценка {removed}')
                else:
                    print("Ошибка: неверный индекс.")
            except ValueError:
                print("Ошибка: введите число.")
        else:
            print('Ошибка: неверное имя ученика или предмет.')

    elif command == 5:  # Редактировать оценку
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f'Оценки: {students_marks[student][class_]}')
            try:
                index = int(input('Введите индекс оценки для изменения (начиная с 0): '))
                if 0 <= index < len(students_marks[student][class_]):
                    new_mark = int(input('Введите новую оценку: '))
                    students_marks[student][class_][index] = new_mark
                    print("Оценка изменена.")
                else:
                    print("Ошибка: неверный индекс.")
            except ValueError:
                print("Ошибка: введите число.")
        else:
            print('Ошибка: неверное имя ученика или предмет.')

    elif command == 6:  # Добавить нового ученика
        new_student = input("Введите имя нового ученика: ")
        if new_student not in students_marks:
            students.append(new_student)
            students.sort()
            students_marks[new_student] = {class_: [] for class_ in classes}
            print(f'Ученик {new_student} добавлен.')
        else:
            print("Такой ученик уже есть.")

    elif command == 7:  # Удалить ученика
        student = input("Введите имя ученика для удаления: ")
        if student in students_marks:
            students.remove(student)
            del students_marks[student]
            print(f'Ученик {student} удален.')
        else:
            print("Ошибка: такого ученика нет.")

    elif command == 8:  # Добавить новый предмет
        new_class = input("Введите название нового предмета: ")
        if new_class not in classes:
            classes.append(new_class)
            for student in students_marks:
                students_marks[student][new_class] = []
            print(f'Предмет {new_class} добавлен.')
        else:
            print("Такой предмет уже есть.")

    elif command == 9:  # Удалить предмет
        del_class = input("Введите название предмета для удаления: ")
        if del_class in classes:
            classes.remove(del_class)
            for student in students_marks:
                students_marks[student].pop(del_class, None)
            print(f'Предмет {del_class} удален.')
        else:
            print("Ошибка: такого предмета нет.")

    elif command == 10:  # Показать все оценки конкретного ученика
        student = input("Введите имя ученика: ")
        if student in students_marks:
            print(student)
            for class_ in students_marks[student]:
                print(f'\t{class_} - {students_marks[student][class_]}')
        else:
            print("Ошибка: такого ученика нет.")

    elif command == 11:  # Показать средний балл по каждому предмету для конкретного ученика
        student = input("Введите имя ученика: ")
        if student in students_marks:
            print(student)
            for class_ in students_marks[student]:
                marks = students_marks[student][class_]
                if marks:
                    avg = sum(marks) / len(marks)
                    print(f'{class_} - {avg:.2f}')
                else:
                    print(f'{class_} - нет оценок')
        else:
            print("Ошибка: такого ученика нет.")

    elif command == 12:  # Выход
        print("Выход из программы.")
        break

    else:
        print("Ошибка: неизвестная команда.")
