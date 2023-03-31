import random
import time
import tkinter

array = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 1

root = tkinter.Tk()
root.title("DeepQ")

frm = tkinter.Frame(root)


def get_description(number, final_pass):
    text = "Pass no."
    if final_pass:
        return " FINAL "

    return text + str(number)


def draw(status, description):
    frm.grid()

    tkinter.Label(frm, text=description, font=("Helvetica", 20)).grid(column=0, row=0)
    tkinter.Label(frm, text="L-weight", font=("Helvetica", 20)).grid(column=0, row=1)
    tkinter.Label(frm, text="R-weight", font=("Helvetica", 20)).grid(column=0, row=2)
    tkinter.Label(frm, text="E="+str("{:.2f}".format(EPSILON)), font=("Helvetica", 20)).grid(column=8, row=1, rowspan=2)

    for i in range(6):
        if i == status:
            tkinter.Label(frm, text="☒", font=("Helvetica", 100)).grid(column=i+1, row=0)
            continue

        tkinter.Label(frm, text="☐", font=("Helvetica", 100)).grid(column=i+1, row=0)

        tkinter.Label(frm, text=str("{:.1e}".format(array[0][i])), font=("Helvetica", 20)).grid(column=i + 1, row=1)
        tkinter.Label(frm, text=str("{:.1e}".format(array[1][i])), font=("Helvetica", 20)).grid(column=i + 1, row=2)

    if status != 7:
        tkinter.Label(frm, text="☑", font=("Helvetica", 100)).grid(column=8, row=0)
    else:
        tkinter.Label(frm, text="☒", font=("Helvetica", 100)).grid(column=8, row=0)

    frm.update()
    time.sleep(0.10)


def get_reward(state):
    if state == 6:
        return 1

    return 0


def next_move(state):
    if random.randrange(0, 1) < EPSILON:
        if random.randint(0, 1) == 1:
            return 1

        return -1

    if array[0][state] == 0 and array[1][state] == 0:
        if random.randint(0, 1) == 1:
            return 1

        return -1

    if array[0][state] > array[1][state]:
        return -1

    if array[0][state] < array[1][state]:
        return 1


def calculate_reward(move, state, next_state):
    if move == -1:
        move = 0

    array[move][state] = array[move][state] + ALPHA*(get_reward(next_state) + (GAMMA*max(array[0][next_state], array[1][next_state])) - array[move][state])


def one_pass(final_pass):
    state = 0
    global number_of_steps

    number_of_steps += 1
    while state != 6:
        draw(state, get_description(number_of_steps, final_pass))

        move = next_move(state)
        next_state = max(state+move, 0)

        calculate_reward(move, int(state), next_state)

        state = next_state

        if final_pass:
            time.sleep(0.4)

    draw(7, get_description(number_of_steps, final_pass))


number_of_steps = 0

while EPSILON > 0:
    one_pass(False)
    EPSILON = EPSILON - 0.15

EPSILON = 0

one_pass(True)

root.mainloop()


