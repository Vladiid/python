#Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

#Формат входных данных
#На вход программе подается пять целых чисел, каждое на отдельной строке.

#Формат выходных данных
#Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.

n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int(input()), int(input())
x = min(n1, n2, n3, n4, n5)
y = max(n1, n2, n3, n4, n5)
print('Наименьшее число =', x)
print('Наибольшее число =', y)