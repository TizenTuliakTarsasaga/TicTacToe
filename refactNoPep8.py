players = [0, '\u001b[33mX', '\u001b[31;1mO']
listField = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def surface():
    print("\u001b[38;5;8m{}\u001b[0m | \u001b[38;5;8m{}\033[1;m | \u001b[38;5;8m{}\033[1;m".format(
        listField[0], listField[1], listField[2]))
    print("---------")
    print("\u001b[38;5;8m{}\u001b[0m | \u001b[38;5;8m{}\033[1;m | \u001b[38;5;8m{}\033[1;m".format(
        listField[3], listField[4], listField[5]))
    print("---------")
    print("\u001b[38;5;8m{}\u001b[0m | \u001b[38;5;8m{}\033[1;m | \u001b[38;5;8m{}\033[1;m".format(
        listField[6], listField[7], listField[8]))


def userInput():
    while True:
        try:
            ui = int(input("\nChoose a cell: "))
        except ValueError:
            print("Not integer!")
            continue
        if ui not in listField:
            print("Wrong input!")
            continue
        else:
            return ui
            break
    print()


def place_marker(listField, ui):
    listField[ui-1] = players[turn]


def winChecker(listField, player):
    return ((listField[0] == listField[1] == listField[2] == player) or
            (listField[3] == listField[4] == listField[5] == player) or
            (listField[6] == listField[7] == listField[8] == player) or
            (listField[0] == listField[3] == listField[6] == player) or
            (listField[1] == listField[4] == listField[7] == player) or
            (listField[2] == listField[5] == listField[8] == player) or
            (listField[0] == listField[4] == listField[8] == player) or
            (listField[2] == listField[4] == listField[6] == player))


def full_check(listField):
    return ((1 not in listField[::]) and
            (2 not in listField[::]) and
            (3 not in listField[::]) and
            (4 not in listField[::]) and
            (5 not in listField[::]) and
            (6 not in listField[::]) and
            (7 not in listField[::]) and
            (8 not in listField[::]) and
            (9 not in listField[::]))


game_on = True

while True:
    print()
    turn = -1
    player = players[turn]

    while game_on:
        surface()
        ui = userInput()
        place_marker(listField, ui)
        print('\n'*100)
        surface()
        if winChecker(listField, player):
            print('\n'*100)
            surface()
            print('Congratulations! Player '+player+' wins!\u001b[0m')
            game_on = False
            break
        else:
            if full_check(listField):
                print('\n'*100)
                surface()
                print("Draw")
                game_on = False
                break
            else:
                turn *= -1
                player = players[turn]
    else:
        break
