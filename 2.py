# 2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

crane = int(input('Введите чётное количество журавликов: '))

Petya = crane / 6
Ceryeja = crane / 6
Katya = (Petya + Ceryeja) * 2

print(f'Количество журавликов: {crane} -> {Petya} {Katya} {Ceryeja}')
