ask = input("введите строку с фруктами через запятую: ")

fruits = list(ask.split(","))#1
print("1:", fruits)

stripped_fruits = [elem.strip() for elem in fruits]#2
print("2:", stripped_fruits)

upper_fruits = [elem.capitalize() for elem in stripped_fruits]#3
print("3:", upper_fruits)

sorted_set_of_fruits = sorted(list(set(upper_fruits)))#4, 5
print("4, 5:", sorted_set_of_fruits)

dictionary_of_fruits = dict()
for elem in stripped_fruits:
	dictionary_of_fruits[elem] = stripped_fruits.count(elem)
print("6:", dictionary_of_fruits)

print("самый популярный фрукт: ", max(dictionary_of_fruits, key=dictionary_of_fruits.get))#7

print(tuple(set(stripped_fruits)))
