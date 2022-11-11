board = list(range(1, 10))
win_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print("_____________")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("_____________")


def take_input(token):
    wrongvalue = True
    while wrongvalue:
        value = input('Enter position for ' + token+':')


        value = int(value)
        if value > 9:
            print('enter less than 10')
            continue
        if str(value) not in '123456789':
            print('this field in not empty')
            continue

        if str(board[value-1]) in 'XO':
            print('this field is not empty')
            continue
        board[value-1] = token
        wrongvalue = False


def check_win():
    for el in win_coord:
        if board[el[0]-1] == board[el[1]-1] == board[el[2]-1]:
            return ''+board[el[0]-1]
        else:
            return ' '


def main():
    draw_board()
    notwon = True
    counter = 0
    while notwon and counter < 10:
        if counter % 2 == 0:
            take_input('X')
            draw_board()
        else:
            take_input('O')
            draw_board()
        counter += 1
        print(counter)
        check = check_win()

        if check == ' ':
            pass
        else:
            print('won', check)
            notwon = False






main()
