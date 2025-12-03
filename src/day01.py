import time
from math import floor

from InputHelper import InputHelper

helper = InputHelper(1)
data = helper.load_data()


def turn_dial(position: int, instruction: str) -> tuple[int, int, int]:
    turn_amount = int(instruction[1:])
    if instruction[0] == "L":
        diff = -turn_amount
    else:
        diff = turn_amount
    full_rotations = (floor(turn_amount / 100))

    return abs((position + diff) % 100), full_rotations, (-(turn_amount - 100 * full_rotations) if instruction[0] == "L" else (turn_amount - 100 * full_rotations))


def count_zero_positions(lines):
    current_position = 50
    zero_count = 0
    for line in lines:
        current_position, _, _ = turn_dial(current_position, line)
        if current_position == 0:
            zero_count += 1

    return zero_count


def count_zero_positions_with_password_method(lines) -> int:
    current_position = 50
    zero_count = 0
    for line in lines:
        previous_position = current_position
        current_position, full_rotations, remainder_diff = turn_dial(current_position, line)

        # Any number of rotations passes zero that many times as well
        if full_rotations > 0:
            zero_count += full_rotations

        # Has moved from non-zero to zero this instruction
        if current_position == 0:
            if previous_position != 0:
                zero_count += 1
        else:
            # We are not at 0 right now, check if we overflowed or underflowed
            result = previous_position + remainder_diff
            if previous_position != 0 and (result < 0 or result > 99):
                zero_count += 1

    return zero_count


start = time.time()
task1Count = count_zero_positions(data)
print("The initial position of 0 has been reached {} times, calculated in {:.2f}ms".format(task1Count, (time.time() - start) * 1000))

start = time.time()
task2Count = count_zero_positions_with_password_method(data)
print("The initial position of 0 with the new method has been reached {} times, calculated in {:.2f}ms".format(task2Count, (time.time() - start) * 1000))
