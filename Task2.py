# Проверить число на простоту (т.е. что число делится только на 1 и само на себя)

from numpy import divide


print("Введите число:")
a = int(input())
i = 0
divider = a
div_naib = 0;
flag = False
while divider > 0:
    if (a % divider == 0): 
        i = i + 1

    if (i == 2 and flag == False): 
        div_naib = divider
        flag = True
        
    divider = divider - 1

if (i == 2): print("Число простое")
else: print("Число не является простым")
print("НОД = ", div_naib)
