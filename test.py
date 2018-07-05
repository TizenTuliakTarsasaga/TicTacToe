from tkinter import *
import tkinter.messagebox
import random

click = True
tk = None


def one_vs_one():
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe")

    def play(button):
        global click, tk

        if button["text"] == " " and click:
            button["text"] = "X"
            button.configure(bg="red", fg="grey")
            click = False
        elif button["text"] == " ":
            button['text'] = "O"
            button.configure(bg="green", fg="grey")
            click = True

        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
                button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes':
                main()

        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
                button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
                button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
                button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
                button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
                button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
                button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
                button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes':
                main()

    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)

    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda: play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)

    tk.mainloop()


def one_vs_computer():
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe")
    list_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def play(button):
        global click, tk

        if button["text"] == " " and click:
            button["text"] = "X"
            button.configure(bg="red", fg="grey")
            if button1["text"] == "X":
                list_field[1-1] = "X"
            if button2["text"] == "X":
                list_field[2-1] = "X"
            if button3["text"] == "X":
                list_field[3-1] = "X"
            if button4["text"] == "X":
                list_field[4-1] = "X"
            if button5["text"] == "X":
                list_field[5-1] = "X"
            if button6["text"] == "X":
                list_field[6-1] = "X"
            if button7["text"] == "X":
                list_field[7-1] = "X"
            if button8["text"] == "X":
                list_field[8-1] = "X"
            if button9["text"] == "X":
                list_field[9-1] = "X"
            while True:
                try:
                    x = int(random.choice(list_field))
                except ValueError:
                    continue
                else:
                    break
            list_field[x-1] = "0"

            if list_field[1-1] == "0":
                button1["text"] = "0"
                button1.configure(bg="green", fg="grey")
            if list_field[2-1] == "0":
                button2["text"] = "0"
                button2.configure(bg="green", fg="grey")
            if list_field[3-1] == "0":
                button3["text"] = "0"
                button3.configure(bg="green", fg="grey")
            if list_field[4-1] == "0":
                button4["text"] = "0"
                button4.configure(bg="green", fg="grey")
            if list_field[5-1] == "0":
                button5["text"] = "0"
                button5.configure(bg="green", fg="grey")
            if list_field[6-1] == "0":
                button6["text"] = "0"
                button6.configure(bg="green", fg="grey")
            if list_field[7-1] == "0":
                button7["text"] = "0"
                button7.configure(bg="green", fg="grey")
            if list_field[8-1] == "0":
                button8["text"] = "0"
                button8.configure(bg="green", fg="grey")
            if list_field[9-1] == "0":
                button9["text"] = "0"
                button9.configure(bg="green", fg="grey")

        print(list_field)

        if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
                button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
            answer = tkinter.messagebox.askquestion('X Player wins!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes':
                main()

        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
                button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
                button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
                button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
                button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
                button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
                button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
                button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
            answer = tkinter.messagebox.askquestion('O Player wins!!!', 'Do you want to play again')
            tk.destroy()
            if answer == 'yes':
                main()


    button1 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button1))
    button1.grid(row=1, column=0, sticky=S+N+E+W)

    button2 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button2))
    button2.grid(row=1, column=1, sticky=S+N+E+W)

    button3 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button3))
    button3.grid(row=1, column=2, sticky=S+N+E+W)

    button4 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button4))
    button4.grid(row=2, column=0, sticky=S+N+E+W)

    button5 = Button(tk, text=" ", font=("Times 26 bold"), height=4, width=8, command=lambda: play(button5))
    button5.grid(row=2, column=1, sticky=S+N+E+W)

    button6 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button6))
    button6.grid(row=2, column=2, sticky=S+N+E+W)

    button7 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button7))
    button7.grid(row=3, column=0, sticky=S+N+E+W)

    button8 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button8))
    button8.grid(row=3, column=1, sticky=S+N+E+W)

    button9 = Button(tk, text=" ", font=('Times 26 bold'), height=4, width=8, command=lambda: play(button9))
    button9.grid(row=3, column=2, sticky=S+N+E+W)

    tk.mainloop()

def main():
    question = int(input("[ 1 ] One VS One\n[ 2 ] One VS Computer\nWhat would you like? "))

    if question == 1:
        one_vs_one()
    elif question == 2:
        one_vs_computer()


main()
