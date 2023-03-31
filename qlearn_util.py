from gui import *

number_of_steps = 0


def get_reward(state):
    if state == 6:
        return 1

    return 0


def next_move(state, e):
    if random.randrange(0, 1) < e:
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


def one_pass(final_pass, e):
    state = 0
    global number_of_steps

    number_of_steps += 1
    while state != 6:
        draw(state, get_description(number_of_steps, final_pass), e)

        move = next_move(state, e)
        next_state = max(state+move, 0)

        calculate_reward(move, int(state), next_state)

        state = next_state

        if final_pass:
            time.sleep(0.4)

    draw(7, get_description(number_of_steps, final_pass), e)
