# Семинар 5
# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой.
#  За один ход можно забрать не более чем 28 конфет. 
#  Все конфеты оппонента достаются сделавшему последний ход.
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
# import random
# def chel_vs_chel():
#     total=2021
#     max_candy=28
#     count=1
#     plaer1=input('Игрок номер 1 представьтесь ')
#     plaer2=input('Игрок номер 2 представьтесь ')
#     x=random.randint(0,1)
#     if x==1:
#         first=plaer1
#         two=plaer2
#     else:
#         first=plaer2
#         two=plaer1
#     print(f'Итак, по результатам честной жеребьевки первым игру начинает {first}')

#     while total>0:
#         if count==1:
#             step=int(input(f'{first} Делайте вашу ставку '))
#             while step>max_candy:
#                 step=int(input(f'Максимум можно только {max_candy} , еще попытка '))
#             total-=step
#         if total>0:
#             print(f'Осталось {total} конфет')
#             count=0
#         else:
#             print('Конфеты кончились')
#         print('Переход хода к сопернику')
#         if count ==0:
#             step=int(input(f'{two} Делайте вашу ставку '))
#             while step>max_candy:
#                 step=int(input(f'Максимум можно только {max_candy} , еще попытка '))
#             total-=step
#         if total>0:
#             print(f'Осталось {total} конфет')
#             count=1
#             print('Переход хода к сопернику')
#         else:
#             print('А нет!Конфетки ВСЁ')
#     if count==1:
#         print(f'Победил {first} поздравляем')
#     if count==0:
#         print(f'Победил {two} поздравляем')
# chel_vs_chel()

# with open('zip.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('zip.txt', 'r') as file:
#     my_text = file.readline()
#     text_compression = my_text.split()
# print(my_text)
# def rle_encode(text):
#     enconding = ''
#     prev_char = ''
#     count = 1
#     if not text:
#         return ''

#     for char in text:
#         if char != prev_char:
#             if prev_char:
#                 enconding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         enconding += str(count) + prev_char
#         return enconding
# text_compression = rle_encode(my_text)

# with open('text_compression_RLE_024.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compression}')
# print(text_compression)

# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах
# with open('zip.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('zip.txt', 'r') as file:
#     my_text = file.readline()
#     text_compression = my_text.split()
# print(my_text)
# def rle_encode(text):
#     enconding = ''
#     prev_char = ''
#     count = 1
#     if not text:
#         return ''

#     for char in text:
#         if char != prev_char:
#             if prev_char:
#                 enconding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         enconding += str(count) + prev_char
#         return enconding
# text_compression = rle_encode(my_text)

# with open('text_compression_RLE_024.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compression}')
# print(text_compression)
# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def delit(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     print(my_text)
# Семинар 4
# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# try:
#       n=int(input('Введите число '))
# except:
#       print('Ввести нужно именно целое число')
# list1 = []
# def Factor(n):
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             list1.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         list1.append(n)
#     print(list1)
# Factor(n)
# задача 2 . Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.




# list1=[1,1,2,3,222,2,3,123,12,1,2,1]

# def unic(list1):
#     list2=[]  
#     for i in range(len(list1)):
#          if list1[i] not in list2:
#             list2.append(list1[i])
                
#     print(list2)
# unic(list1)
# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (
#     наименьшее общее кратное) этих двух чисел..
# a=122
# b=4
# def nod(a,b):
#     if b==0:
#         return a
#     else:
#         return nod(b,a%b)
 
# def nok(a,b):
#     print (a*b//nod(a,b))
# nok(a,b)


# Семинар 3
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

# try:
#       n=int(input('Введите число '))
# except:
#       print('Ввести нужно именно целое число')
# def binar(n):
#     b = ''
#     while n > 0:
#         b = str(n % 2) + b
#         n = n // 2
#     print(b)
# binar(n)



        
        

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
