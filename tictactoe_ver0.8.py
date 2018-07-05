import sys
import random
import time
import operator

list_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def surface():
    print("\u001b[38;5;8m{}\u001b[0m | \u001b[38;5;8m{}\033[1;m | \u001b[38;5;8m{}\033[1;m".format(
        list_field[0], list_field[1], list_field[2]))
    print("---------")
    print("\u001b[38;5;8m{}\u001b[0m | \u001b[38;5;8m{}\033[1;m | \u001b[38;5;8m{}\033[1;m".format(
        list_field[3], list_field[4], list_field[5]))
    print("---------")
    print("\u001b[38;5;8m{}\u001b[0m | \u001b[38;5;8m{}\033[1;m | \u001b[38;5;8m{}\033[1;m".format(
        list_field[6], list_field[7], list_field[8]))


def loading_screen():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.01)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()
    print()
    print()


def win_checker():
    if (list_field[0] == "\u001b[33mX" and list_field[1] == "\u001b[33mX" and list_field[2] == "\u001b[33mX" or
        list_field[3] == "\u001b[33mX" and list_field[4] == "\u001b[33mX" and list_field[5] == "\u001b[33mX" or
        list_field[6] == "\u001b[33mX" and list_field[7] == "\u001b[33mX" and list_field[8] == "\u001b[33mX" or
        list_field[0] == "\u001b[33mX" and list_field[3] == "\u001b[33mX" and list_field[6] == "\u001b[33mX" or
        list_field[1] == "\u001b[33mX" and list_field[4] == "\u001b[33mX" and list_field[7] == "\u001b[33mX" or
        list_field[2] == "\u001b[33mX" and list_field[5] == "\u001b[33mX" and list_field[8] == "\u001b[33mX" or
        list_field[0] == "\u001b[33mX" and list_field[4] == "\u001b[33mX" and list_field[8] == "\u001b[33mX" or
            list_field[2] == "\u001b[33mX" and list_field[4] == "\u001b[33mX" and list_field[6] == "\u001b[33mX"):
        print("\n\u001b[33mX WIN!!!!!!")
        sys.exit()

    if (list_field[0] == "\u001b[31;1mO" and list_field[1] == "\u001b[31;1mO" and list_field[2] == "\u001b[31;1mO" or
        list_field[3] == "\u001b[31;1mO" and list_field[4] == "\u001b[31;1mO" and list_field[5] == "\u001b[31;1mO" or
        list_field[6] == "\u001b[31;1mO" and list_field[7] == "\u001b[31;1mO" and list_field[8] == "\u001b[31;1mO" or
        list_field[0] == "\u001b[31;1mO" and list_field[3] == "\u001b[31;1mO" and list_field[6] == "\u001b[31;1mO" or
        list_field[1] == "\u001b[31;1mO" and list_field[4] == "\u001b[31;1mO" and list_field[7] == "\u001b[31;1mO" or
        list_field[2] == "\u001b[31;1mO" and list_field[5] == "\u001b[31;1mO" and list_field[8] == "\u001b[31;1mO" or
        list_field[0] == "\u001b[31;1mO" and list_field[4] == "\u001b[31;1mO" and list_field[8] == "\u001b[31;1mO" or
            list_field[2] == "\u001b[31;1mO" and list_field[4] == "\u001b[31;1mO" and list_field[6] == "\u001b[31;1mO"):
        print("\n\u001b[31;1m0 WIN!!!!!!")
        sys.exit()


def user_input():
    while True:
        try:
            ui = int(input("\nChoose a cell: "))
        except ValueError:
            print("Not integer!")
            continue
        if ui not in list_field:
            print("Wrong input!")
            continue
        else:
            list_field[ui-1] = "\u001b[31;1mO"
            break
    print()


def user_input_2():
    while True:
        try:
            ui = int(input("\nChoose a cell: "))
        except ValueError:
            print("Not integer!")
            continue
        if ui not in list_field:
            print("Wrong input!")
            continue
        else:
            list_field[ui-1] = "\u001b[33mX"
            break
    print()


def computer_step():
    print("\nComputer round:\n")
    loading_screen()
    while True:
        try:
            x = int(random.choice(list_field))
        except ValueError:
            continue
        else:
            break
    list_field[x-1] = "\u001b[33mX"


def firstStep():

    list_field[4] = "\u001b[33mX"


def computer_AI():
    row1 = [10, 10, 10]
    row2 = [10, 10, 10]
    row3 = [10, 10, 10]
    col1 = [10, 10, 10]
    col2 = [10, 10, 10]
    col3 = [10, 10, 10]
    arc1 = [10, 10, 10]
    arc2 = [10, 10, 10]

    if list_field[0] == "\u001b[31;1mO":
        row1[0] -= 5
        col1[0] -= 5
        arc1[0] -= 5
    if list_field[1] == "\u001b[31;1mO":
        row1[1] -= 5
        col2[0] -= 5
    if list_field[2] == "\u001b[31;1mO":
        row1[2] -= 5
        col3[0] -= 5
        arc2[0] -= 5
    if list_field[3] == "\u001b[31;1mO":
        row2[0] -= 5
        col1[1] -= 5
    if list_field[4] == "\u001b[31;1mO":
        row2[1] -= 5
        col2[1] -= 5
        arc1[1] -= 5
        arc2[1] -= 5
    if list_field[5] == "\u001b[31;1mO":
        row2[2] -= 5
        col3[1] -= 5
    if list_field[6] == "\u001b[31;1mO":
        row3[0] -= 5
        col1[2] -= 5
        arc2[2] -= 5
    if list_field[7] == "\u001b[31;1mO":
        row3[1] -= 5
        col2[2] -= 5
    if list_field[8] == "\u001b[31;1mO":
        row3[2] -= 5
        col3[2] -= 5
        arc1[2] -= 5

    if list_field[0] == "\u001b[33mX":
        row1[0] += 1
        col1[0] += 1
        arc1[0] += 1
    if list_field[1] == "\u001b[33mX":
        row1[1] += 1
        col2[0] += 1
    if list_field[2] == "\u001b[33mX":
        row1[2] += 1
        col3[0] += 1
        arc2[0] += 1
    if list_field[3] == "\u001b[33mX":
        row2[0] += 1
        col1[1] += 1
    if list_field[4] == "\u001b[33mX":
        row2[1] += 1
        col2[1] += 1
        arc1[1] += 1
        arc2[1] += 1
    if list_field[5] == "\u001b[33mX":
        row2[2] += 1
        col3[1] += 1
    if list_field[6] == "\u001b[33mX":
        row3[0] += 1
        col1[2] += 1
        arc2[2] += 1
    if list_field[7] == "\u001b[33mX":
        row3[1] += 1
        col2[2] += 1
    if list_field[8] == "\u001b[33mX":
        row3[2] += 1
        col3[2] += 1
        arc1[2] += 1

    row_b1 = [1, 2, 3]
    row_b2 = [4, 5, 6]
    row_b3 = [7, 8, 9]
    col_b1 = [1, 4, 7]
    col_b2 = [2, 5, 8]
    col_b3 = [3, 6, 9]
    acr_b1 = [1, 5, 9]
    acr_b2 = [3, 5, 7]

    orderList = [sum(row1), sum(row2), sum(row3), sum(col1), sum(col2), sum(col3), sum(arc1), sum(arc2)]
    stepDict = {int(sum(row1)): 1, int(sum(row2)): 2, int(sum(row3)): 3, int(sum(col1)): 4, int(sum(col2)): 5, int(
        sum(col3)): 6, int(sum(arc1)): 7, int(sum(arc2)): 8}
    aimax = max(orderList)
    aimin = min(orderList)

    def chooser(x):
        if x == 1:
            y = random.choice(row_b1)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(1)
        elif x == 2:
            y = random.choice(row_b2)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(2)
        elif x == 3:
            y = random.choice(row_b3)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(3)
        elif x == 4:
            y = random.choice(col_b1)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(4)
        elif x == 5:
            y = random.choice(col_b2)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(5)
        elif x == 6:
            y = random.choice(col_b3)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(6)
        elif x == 7:
            y = random.choice(acr_b1)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(7)
        elif x == 8:
            y = random.choice(acr_b2)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(8)
        elif x == 9:
            y = random.randint(1, 9)
            if y in list_field:
                list_field[y-1] = "\u001b[33mX"
            else:
                chooser(9)

    if aimax >= 32:
        weight = stepDict.get(aimax)
    elif aimin == 20:
        weight = stepDict.get(aimin)
    elif sum(orderList) < 224:
        weight = 9
    else:
        weight = stepDict.get(aimax)

    chooser(weight)


def main():
    question = int(input("[ 1 ] 1 vs 1 \n[ 2 ] 1 vs cpu\n[ 3 ] 1 vs cpu Advenced\n\nWhat would you like: "))

    if question == 1:
        print()
        counter = 0

        while counter <= 3:
            print(list_field)
            surface()
            win_checker()
            user_input_2()
            print(list_field)
            surface()
            win_checker()
            user_input()

            counter = counter + 1

        print(list_field)
        surface()
        win_checker()
        user_input_2()
        print(list_field)
        surface()
        win_checker()
        print()
        print("Draw")

    elif question == 2:
        print()
        counter = 0

        while counter <= 3:
            print(list_field)
            surface()
            win_checker()
            loading_screen()
            computer_step()
            print(list_field)
            surface()
            win_checker()
            user_input()

            counter = counter + 1

        print(list_field)
        surface()
        win_checker()
        loading_screen()
        computer_step()
        print(list_field)
        surface()
        win_checker()
        print()
        print("Draw")

    elif question == 3:
        print()
        counter = 0
        win_checker()
        firstStep()
        surface()
        print()
        win_checker()
        user_input()

        while counter <= 2:
            surface()
            print()
            win_checker()
            computer_AI()
            surface()
            print()
            win_checker()
            user_input()

            counter = counter + 1

        surface()
        print()
        win_checker()
        computer_AI()
        surface()
        print()
        print("Draw")

if __name__ == '__main__':
    main()
