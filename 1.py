#  1. Найдите сумму цифр трехзначного числа.
#  Пример:
#  123 -> 6 (1 + 2 + 3)
#  100 -> 1 (1 + 0 + 0)

number = int(input('Введитe трёхзначное число: '))

a = (number / 100)//1
b = ((number % 100) / 10) // 1
c = number % 10

sum = a + b + c

print(f'{number} -> {sum} ({a} + {b} + {c})')
