from random import randint

# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

n = 8
not_beat_queen = True
x_list = []
y_list = []

def is_solve_queens() -> bool:
    global n, x_list, y_list, not_beat_queen    

    for i in range(n):
        x, y = [int(coordinate) 
                for coordinate in input("Введите координаты ферзя (сначала x, затем y, через пробел)").split()]
        x_list.append(x)
        y_list.append(y)

    for i in range(n):
        for j in range(i + 1, n):
            if x_list[i] == x_list[j] or y_list[i] == y_list[j] or \
            abs(x_list[i] - x_list[j]) == abs(y_list[i] - y_list[j]):
                not_beat_queen = False
                x_list = []
                y_list = []
                return not_beat_queen
    if not_beat_queen:
        x_list = []
        y_list = []
        return not_beat_queen 

if __name__ == '__main__':
    print(is_solve_queens())
# 3 0     1 1    6 2    2 3    5 4    7 5    4 6    0 7   True
# 0 5     1 2    2 6    3 1    4 7    5 4    6 0    7 3   True