# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = int(input())
# a = n // 100
# b = n % 100 // 10
# c = n % 10
# print(f'{a + b + c} = {a} + {b} + {c}')

# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# s = int(input("Введите количество журавликов, число должно быть кратно 6: "))
# print(int(s / 6), int(s * 2 / 3), int(s / 6))

# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = int(input("Введите шестизначный номер вашего билета: "))
# a = n // 100000
# b = n % 100000 // 10000
# c = n % 10000 // 1000
# d = n % 1000 // 100
# e = n % 100 // 10
# m = n % 10
# if a + b + c == d + e + m:
#     print("YES!!! ")
# else:
#     print("NO ")

# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# m, n, k = int(input()), int(input()), int(input())
# if k % m == 0 or k % n == 0:
#      print('yes')
# else:
#      print('no')


