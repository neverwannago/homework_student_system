from functools import reduce
from sys import exit
menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}



def print_menu():
    sorted_by_name = sorted(menu.items(), key=lambda x: x[0])
    sorted_by_price = sorted(menu.items(), key=lambda x: x[1])
    
    choice = input("как вы хотите cортировать?\n 1. по названию\n 2. по цене\nваш выбор: ")
    print("\nменю:")
    if choice == '1': # не знаю как грамотно оформить, пусть будет так
        for name, price in sorted_by_name:
            print(f"{name} - {price} руб.")
    elif choice == '2':
        for name, price in sorted_by_price:
            print(f"{name} - {price} руб.")
    else:
        print("неверный ввод")

def average():
    average_ariphmetic = lambda menu : sum(menu.values())/len(menu)
    print(f"средняя цена в меню: {average_ariphmetic(menu)} руб.")

def update_menu(): 
    try:
        new_food = input("введите блюдо:")
        new_price = int(input("введите цену новому блюду:"))
        update = lambda food, price: menu.update({food: price})
        update(new_food, new_price)
    except ValueError:
        print("введите корректные данные")
        main_menu()

def delete_food():
    item = input("введите блюдо для удаления: ").strip()
    delete_food = lambda food : menu.pop(food) if food in menu else print("такой еды нет")
    return delete_food(item)

def show_cheaper(): #не работает
    try:
        price = int(input("введите прайс: "))
        cheaper = filter(lambda x: x[1] < price, menu.items())
        for name, price in cheaper:
            print(f"{name}: {price} руб.")
    except ValueError:
        print("введите нормальный прайс.")

def min_max_food():
    mini = min(menu.items(), key=lambda value : value[1])
    maxi = max(menu.items(), key=lambda value : value[1])  
    print(f"самое дешевое - {mini[0]}, {mini[1]} рублей.")
    print(f"самое дорогое - {maxi[0]}, {maxi[1]} рублей.")

def show_drinks():
    target_food = ["coffee", "tea", "juice"]
    drinks = filter(lambda x: x[0] in target_food, menu.items())
    sorted_drinks = sorted(drinks, key=lambda x: x[1])
    for name, price in sorted_drinks:
        print(f"{name}: {price} руб.")

def order():
    user_order = input("введите блюда через запятую: ")
    user_food = list(map(lambda x : x.strip(), user_order.split(',')))#короче map соединяет ламбду с убиранием пробелов, и все это дело происходит со списком
    #такие дела
    valid_food = filter(lambda x: x in menu, user_food)

    order = {food: menu[food] for food in valid_food}#заказ

    #обрабатываем заказ дальше
    if not any(order):
        print("вы ниче не выбрали..")
        main_menu()
    total_price = reduce(lambda x, y: x + y, order.values())

    print("ваш заказ:")
    for num, food_tuple in enumerate(order.items(), 1):
        item, price = food_tuple
        #че здесь произошло?
        #короче здесь начинаем нумерацию с единичку и по идее у нас это все дело дается как [(1, ('food', price))]
        #поэтому здесь делается такая тема
        print(f"{num}. {item.capitalize()} — {price} руб.")
    print(f"итого: {total_price} руб.")

    if total_price > 500:
        print("вам добавляется скидка 10%!")
        print(f"к оплате: {total_price * 0.9:.2f} руб.")

def exit_lol():
    print("выходим..")
    exit()



variations_of_choices = {
    '1': print_menu,
    '2': average,
    '3': update_menu,
    '4': delete_food,
    '5': show_cheaper,
    '6': min_max_food,
    '7': show_drinks,
    '8': order,
    '0': exit_lol
}

def main_menu():
    print('''
что вы хотите сделать?
1. Вывести всё меню.
2. Посчитать среднюю цену блюда в меню.
3. Добавить новые блюда в меню. Если блюдо уже есть, то заменить цену.
4. Удалить блюдо из меню.
5. Показать все блюда дешевле определённой цены.
6. Найти самое дешёвое и самое дорогое блюдо.
7. Сделать список только напитков и отсортировать их по цене.
8. Сделать заказ.
0. Выход.''')
        
    choice = input("ваш выбор: ")
    if choice in variations_of_choices:
        variations_of_choices[choice]()
        print("\nхотите продолжить?")
        main_menu()
    else:
        print("некорректный выбор")
        main_menu()
main_menu()
