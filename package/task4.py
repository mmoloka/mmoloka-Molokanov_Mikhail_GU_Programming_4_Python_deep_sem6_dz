# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки 
# ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

board = [[0 for x in range(8)] for y in range(8)]  # доска 8х8 заполнена нулями

def set_queen(x, y):
    '''Ставим ферзя (-1) на клетку с координатами x, y, закрашиваем (1) клетки, которые он бьет.'''
    for i in range(8):
        board[i][y] += 1
        board[x][i] += 1
        if 0 <= x + y - i < 8:
            board[x + y - i][i] += 1 
        if 0 <= x - y + i < 8:
            board[x - y + i][i] += 1
    board[x][y] = -1

def remove_queen(x, y):
    '''Убираем ферзя с клетки с координатами x, y, затираем все -1 и 1 в 0'''
    for i in range(8):
        board[i][y] -= 1
        board[x][i] -= 1
        if 0 <= x + y - i < 8:
            board[x + y - i][i] -= 1 
        if 0 <= x - y + i < 8:
            board[x - y + i][i] -= 1
    board[x][y] = 0

def print_solve():
    '''Вывод на печать решения задачи в виде последовательности кортежей с координатами ферзей'''
    solve_list = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                solve_list.append((i, j))
    print(*solve_list, sep='; ')            

def solve(x):
    '''Ищем пустую клетку для ферзя от первой строки рекурсивно до последней строки - выводим решение'''
    for y in range(8):
        if board[x][y] == 0:
            set_queen(x, y)
            if x == 7:
                print_solve()
            else:
                solve(x + 1)
            remove_queen(x, y)    

if __name__ == '__main__':
    solve(0)
