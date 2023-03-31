import random

array = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

ALPHA = 0.1
GAMMA = 0.9
EPSILON = 1


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
        if randint(0, 1) == 1:
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


def one_pass():
    state = 0

    while state != 6:
        move = next_move(state)
        next_state = max(state+move, 0)

        calculate_reward(move, int(state), next_state)

        state = next_state


number_of_steps = 0

while max(array[0][0], array[1][0]) == 0:
    one_pass()
    EPSILON = EPSILON - 0.1
    number_of_steps = number_of_steps + 1

print("number of passes = ", number_of_steps)
print("Weights L = ", array[0])
print("Weights P = ", array[1])
