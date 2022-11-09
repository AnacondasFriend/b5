M = [['-','-','-'],['-','-','-'],['-','-','-']]

def m_print():
    print('  0 1 2')
    for i in range(3):
        print(i, ' '.join(M[i]))

def who_win():
    if any([
    M[0][0] == 'X' and M[0][1] =='X' and M[0][2] == 'X',
    M[1][0] == 'X' and M[1][1] =='X' and M[1][2] == 'X',
    M[2][0] == 'X' and M[2][1] =='X' and M[2][2] == 'X',
    M[0][0] == 'X' and M[1][0] =='X' and M[2][0] == 'X',
    M[0][1] == 'X' and M[1][1] =='X' and M[2][1] == 'X',
    M[0][2] == 'X' and M[1][2] =='X' and M[2][2] == 'X',
    M[0][0] == 'X' and M[1][1] =='X' and M[2][2] == 'X',
    M[0][2] == 'X' and M[1][1] =='X' and M[2][0] == 'X']):
        print("Крестики поибедили!")
        return 0
    elif any([
    M[0][0] == 'O' and M[0][1] =='O' and M[0][2] == 'O',
    M[1][0] == 'O' and M[1][1] =='O' and M[1][2] == 'O',
    M[2][0] == 'O' and M[2][1] =='O' and M[2][2] == 'O',
    M[0][0] == 'O' and M[1][0] =='O' and M[2][0] == 'O',
    M[0][1] == 'O' and M[1][1] =='O' and M[2][1] == 'O',
    M[0][2] == 'O' and M[1][2] =='O' and M[2][2] == 'O',
    M[0][0] == 'O' and M[1][1] =='O' and M[2][2] == 'O',
    M[0][2] == 'O' and M[1][1] =='O' and M[2][0] == 'O']):
        print("Нолики поибедили!")
        return 0
    elif all([
    M[0][0] != '-', M[0][1] !='-', M[0][2] != '-',
    M[1][0] != '-' and M[1][1] !='-' and M[1][2] != '-',
    M[2][0] != '-' and M[2][1] !='-' and M[2][2] != '-']):
        print('Ничья. Победила дружба:)')
        return 0
    else:
        return 1

def inputik(string):
    i = int(input(f'Ходит {string}. \nВведите номер строки '))
    j = int(input('Введите номер столбца '))
    if i >= 3 or j >= 3:
        print('Ошибка! Строка/столбец должны быть от 0 до 2х. Введите данные еще раз.')
        i,j = inputik(string)
    return i, j

def x_func():
    #i = int(input('Ходит крестик. \nВведите номер строки '))
    #j = int(input('Введите номер столбца '))
    i, j = inputik('крестик')
    if M[i][j] != '-':
        print('Эта ячейка занята. Выберите другую.')
        x_func()
    else:
        M[i][j] = 'X'
        m_print()

def o_func():
    i, j = inputik('нолик')
    if M[i][j] != '-':
        print('Эта ячейка занята. Выберите другую.')
        o_func()
    else:
        M[i][j] = 'O'
        m_print()


print('Добро пожаловать на самую кибервинтажную игру 21 века - крестики и нолики!!!!')
m_print()

while who_win():
    x_func()
    if who_win() == 0:
        break
    o_func()
    if who_win() == 0:
        break
