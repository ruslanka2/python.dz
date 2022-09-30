# Задача 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# list1 = [2, 3, 5, 9, 3]

# def nechet(list1):
#     sum = 0
#     for i in range(1, len(list1)):
#         if i % 2 == 1:
#             sum += list1[i]
#     print(sum)

# print(list1)
# nechet(list1)
# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# list1=[2, 3, 4, 5, 6]
# def pro(list1):
#     counter1=-1
#     prooz=1
#     for i in range((len(list1)+1)//2):
#         prooz=list1[i]*list1[counter1]
#         counter1-=1
#         print(prooz)
# print(list1)
# pro(list1)

# задача 3

# list1=[1.1, 1.2, 3.1, 5.5, 10.01]
# drobn=[]
# def drob(list1):
#     m=0
#     for i in range(len(list1)):
#         m=round (float(list1[i])-int(list1[i]),2)
#         drobn.append(m)
#     print(drobn)
# drob(list1)
# def razn(drobn):
#     maxi=drobn[0]
#     mini=drobn[1]
#     for i in range(len(drobn)):
#         if drobn[i]>maxi:
#             maxi=drobn[i]
#         if drobn[i]<mini:
#             mini=drobn[i]
#     print(maxi-mini)
# razn(drobn)

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

try:
      n=int(input('Введите число '))
except:
      print('Ввести нужно именно целое число')
def binar(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)
binar(n)



        
        

#  seminar 2
# Задача 1. Напишите программу, которая принимает на вход вещественное или целое
# число и показывает сумму его цифр. Через строку нельзя решать.
# num=input('введите число ')
# p=0
# if num.isdigit():
#     num=int(num)
#     while num!=0:
#         p=p+num%10
#         num=num//10
#     print(p)
# else:
#     x=num.split('.')
#     a=int(x[0])
#     b=int(x[1])
#     while a!=0:
#         p=p+a%10
#         a=a//10
#     while b!=0:
#         p=p+b%10
#         b=b//10
#     print(p)
# Задача 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# num=int(input('Введите число '))
# p=1
# for i in range(1,num+1):
#     p*=i
#     print(f'{p}', end=' ')

# Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами,
#  выводится на экран,
#  затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!
# import random
# N=10
# spisok=[]
# for i in range(N):
#     spisok.append(random.randint(1,100))
# print(spisok)

# def bubble(spisok):
#     for i in range(N-1):
#         for j in range(N-i-1):
#             if spisok[j] > spisok[j+1]:
#                 buff = spisok[j]
#                 spisok[j] = spisok[j+1]
#                 spisok[j+1] = buff
# bubble(spisok)
# print(spisok)
# Seminar1
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
