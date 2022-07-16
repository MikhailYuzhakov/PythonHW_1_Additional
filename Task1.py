# Найти факториал числа

res = 1

print("Введите число: ")
a = int(input())

for i in range(a):
    res = res * (i + 1)

print(a,'! = ',res)
