# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# -
# try:
#     print('введите день недели')
#     a=int(input())
#     def res():
#         if (a<0 or a>7):
#             return 'Это не день недели'
#         if (a<=5):
#                 return 'нет'
#         else:
#                 return 'выходной день'
#     print(res())
# except:
#     print('Некорректный ввод')

# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
#  эта точка (или на какой оси она находится).
# try:
#     print('введите координаты точки X')
#     a=int(input())
#     print('введите координаты точки Y')
#     b=int(input())
#     def obl():
#         if(a>0 and b>0):
#             return '1'
#         if(a<0 and b>0):
#             return '2'
#         if(a<0 and b<0):
#             return '3'
#         if(a>0 and b<0):
#             return '4'
#     print(obl())
# except:
#     print('Некорректный ввод')
# try:
#     def inputNumbers(x):
#         xyz = ["X", "Y", "Z"]
#         a = []
#         for i in range(x):
#             a.append(input(f"Введите значение {xyz[i]}: "))
#         return a
#     def prover(x):
#      left = not (x[0] or x[1] or x[2])
#      right = not x[0] and not x[1] and not x[2]
#      result = left == right
#      return result
#     statement = inputNumbers(3)

#     if prover(statement) == True:
#           print(f"Утверждение истинно")
#     else:
#           print(f"Утверждение ложно")
# except:
#     print('Некорректный ввод')
# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.



# try:
#     import random
#     print('введите колличество строк')
#     m=int(input())
#     print('введите колличество столбцов')
#     n=int(input())
#     def create_array(m,n):
#         array_2d=[]
#         for i in range(m):
#             second_arr=[]
#             for j in range(n):
#                 second_arr.append(random.randint(1,10))
#             array_2d.append(second_arr)
#         return array_2d
    
    
#     def print_array(array_2d,m,n):
#         for i in range(m):
#             for j in range(n):
#                 print(array_2d[i][j], end=' ')
#             print()
#     print(print_array)
#     ar=create_array(m,n)
#     print_array(ar)
# except:
#         print('Некорректный ввод')