'''Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке
есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.'''

a = input()
print('YES' if 'суббота' in a or 'воскресенье' in a else 'NO')

