import time
from itertools import combinations

from InputHelper import InputHelper

helper = InputHelper(3)
data = helper.load_data()


def get_largest_joltage_for_row(row) -> int:
    largest_digit = 0
    second_largest_digit = 0

    for i in range(len(row) - 1):
        current_digit = int(row[i])
        next_digit = int(row[i + 1])

        if current_digit > largest_digit:
            largest_digit = current_digit
            second_largest_digit = next_digit
        else:
            if next_digit > second_largest_digit:
                second_largest_digit = next_digit

    return largest_digit * 10 + second_largest_digit


def get_largest_joltage_with_more_power(row) -> int:
    options = combinations(list(row), 12)
    possible_jolts = []
    for option in options:
        jolt_value = sum([int(x) * (pow(10, 12 - i)) for i, x in enumerate(option)])
        possible_jolts.append(jolt_value)

    return max(possible_jolts)


def get_sum_of_largest_joltages(rows) -> int:
    return sum([get_largest_joltage_for_row(r) for r in rows])


def get_sum_of_largest_joltages_with_more_power(rows) -> int:
    return sum([get_largest_joltage_with_more_power(r) for r in rows])


start = time.time()
task1Sum = get_sum_of_largest_joltages(data)
print("The sum of the joltages is {}, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = get_sum_of_largest_joltages_with_more_power(data)
print("The sum of the joltages with more power is {}, calculated in {:.2f}ms".format(task2Sum, (time.time() - start) * 1000))
