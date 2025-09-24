import csv
from sys import exit

students = {

}

def add_student():
    try:
        name = input("имя: ").strip().lower().capitalize()
        age = int(input("возраст только цифрами: "))
        grades = input("введите оценки через запятые: ")
        list_of_grades = ([int(elem.strip()) for elem in grades.split(",")])
        #конструкция выше делает из grades список через split, там перебираются элементы,
        #к ним применяется strip на уборку пробелов, и все закидывается в int
        other_info = {"age":age, "grades":list_of_grades}
        result = {f"{name}": other_info}
    except ValueError:
        print("вы ввели неверное значение, возвращаю в меню..")
    else:
        print("студент успешно добавлен")
        return students.update(result)
    finally:
        print("выполнена функция по добавлению студента.")

def show_all_students():
    if len(students) == 0:
        print("студентов нет в бд ¯\_(ツ)_/¯")
    res = []
    for name, other_data in students.items(): 
        age = other_data.get('age')
        grades = other_data.get('grades')
        res.append(f"Студент {name}: возраст {age} лет, оценки: {grades}")
    print('\n'.join(res))

def find_student():
    given_name = input("имя: ").strip().lower().capitalize()
    res = []
    count=0
    for name, other_data in students.items():
        if given_name == name:#по условию не может быть нескольких людей, ибо это противоречит словарю, в противном случае в задании нужно было указать этот пункт, так что забью
            age = other_data.get('age')
            grades = other_data.get('grades')
            res.append(f"Студент {name}: возраст {age} лет, оценки: {grades}")
            count+=1
    if count == 0:
        res.append("такого студента нет.")
    print('\n'.join(res))

def delete_student():
    given_name = input("имя: ").strip().lower().capitalize()
    if given_name in students:
        students.pop(given_name)
        print(f"студент {given_name} был удален.")
    else:
        print("такого студента нет в базе данных.")
        
def add_grade_to_student():#дается имя студента, мы его вычисляем, затем получаем его оценки через
    try:
        given_name = input("имя: ").strip().lower().capitalize()
        new_grade = int(input("оценка, которую нужно добавить: "))
        for name, other_data in students.items():
            if given_name == name:
                grades = other_data.get('grades')
                print(f"Студент до добавления оценки:\n{name}: оценки:{grades}")
                grades.append(new_grade)
                print(f"\nСтудент после:\n{name}: оценки:{grades}")
            else:
                print("невозможно добавить оценку студенту, которого нет в бд.")
    except ValueError:
        print("введите корректную оценку.")

def show_student_above_custom_age():#передается возраст, все студенты у которых возраст > указанного выводятся
    try:
        given_age = int(input("возраст: "))
        found_student = False
        for name, other_data in students.items():
            age = other_data.get('age')
            if age > given_age:
                grades = other_data.get('grades')
                print(f"Студент {name}: возраст {age} лет, оценки: {grades}")
                found_student = True
        if not found_student:
            print("таких студентов нет.")
    except ValueError:
        print("введите КОРРЕКТНЫЙ возраст.")

def show_student_above_custom_grade():
    try:
        given_grade = int(input("оценка: "))
        found_student = False
        for name, other_data in students.items():
            grades = other_data.get('grades')
            if max(grades) > given_grade:#сравнивается список с числом
                age = other_data.get('age')
                print(f"Студент {name}: возраст {age} лет, оценки: {grades}")
                found_student = True
        if not found_student:
            print("таких студентов нет.")
    except ValueError:
        print("введите КОРРЕКТНУЮ оценку.")

def export_students():#вывести из проги в csv файл студентов
    filename1 = input("введите название, которым будет назван файл БЕЗ указания формата данных:")
    try:
        choice = int(input("теперь укажите тип данных через цифру: \n1.CSV \n2.TXT\n"))
        if choice == 1:
            filename = filename1 + ".csv"
        elif choice == 2:
            filename = filename1 + ".txt"
        else:
            print("некорретный тип данных!")
            main_menu()
    except ValueError:
        print("некорретный тип данных!")
    print("будет экспортирован файл: ", filename)
    with open(filename, 'w') as file:
        writer = csv.writer(file, delimiter=";")
        for name, other_data in students.items(): 
            age = other_data.get('age')
            grades = other_data.get('grades')
            str_grades = ','.join(map(str, grades))
            writer.writerow([name, age, str_grades])
    print("экспортировано успешно")

def import_students():
    filename = input("введите название вашего файла для импорта ВМЕСТЕ с расширением (поддерживаются csv/txt):")
    print("файл: ", filename)
    k=0
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                # k+=1
                # print(f"row number {k}: ", row)
                # print("row[1]: ", row[1])
                if len(row) < 3: #надо, потому что эксель тупо обрабатывает файл
                    continue
                name = row[0]
                age = row[1]
                grades = [int(grade) for grade in row[2].split(",")]
                students.update({f"{name}" : {"age" : age, "grades" : grades}})
        print("импортирование успешно")
    except FileNotFoundError:
        print("такого файла не существует в этой папке!!")

def exiting():
    print("выходим из программы..")
    exit()

# def get_students():
#     print("Студенты: ", students)

variations_of_choices = {
    '1' : add_student,
    '2' : show_all_students,
    '3' : find_student,
    '4' : delete_student,
    '5' : add_grade_to_student,
    '6' : show_student_above_custom_age,
    '7' : show_student_above_custom_grade,
    '8' : export_students, # to csv (name, age, grades)
    '9' : import_students, # to csv
    '10' : exiting,
    # '11' : get_students
}

print("здравствуйте! что вы хотите сделать?:\n")

def main_menu():
    print(
    "1. Добавить студента (имя, возраст, список оценок).\n",
    "2. Показать всех студентов.\n",
    "3. Найти студента по имени.\n",
    "4. Удалить студента.\n",
    "5. Добавить новую оценку студенту.\n",
    "6. Вывести список студентов старше определённого возраста.\n",
    "7. Показать всех студентов с оценкой выше определённого порога.\n",
    "8. Экспортировать список студентов в CSV-вид (имя;возраст;оценки).\n",
    "9. Импортировать студентов из CSV.\n",
    "10. Выход.\n"
    )

    choice = input("ваш выбор: ")
    if choice in variations_of_choices:
        variations_of_choices[choice]()
        print("\nхотите продолжить?")
        main_menu()
    else:
        print("некорректный выбор")
        main_menu()
main_menu()
