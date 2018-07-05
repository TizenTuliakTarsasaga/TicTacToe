
players = [0 ,'\u001b[33mX','\u001b[31;1mO']
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
    (listField[3] ==  listField[4] ==  listField[5] == player) or
    (listField[6] ==  listField[7] ==  listField[8] == player) or
    (listField[0] ==  listField[3] ==  listField[6] == player) or
    (listField[1] ==  listField[4] ==  listField[7] == player) or
    (listField[2] ==  listField[5] ==  listField[8] == player) or
    (listField[0] ==  listField[4] ==  listField[8] == player) or
    (listField[2] ==  listField[4] ==  listField[6] == player))


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


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('\n'*100)
game_on = True
question = int(input("[1] 1 vs 1 \n[2] 1 vs cpu\n[3] 1 vs cpu Advenced What would you like: "))

if question == 1:
    while True:
        print()
        turn = -1
        player = players[turn]
        while game_on:
            surface()        
            ui = userInput()
            place_marker(listField, ui)
            surface()
            if winChecker(listField, player):
                surface()
                print('Congratulations! Player '+player+' wins!\u001b[0m')
                listField = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                if not replay():
                    break
            else:
                if full_check(listField):
                    surface()
                    print("Draw")
                    break
                else:
                    turn *= -1
                    player = players[turn]
                    print(player)
        listField = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if not replay():
            break
