import time
from math import floor

from InputHelper import InputHelper

helper = InputHelper(2)
data = helper.load_data(as_string=True)


def get_invalid(shop_id: int, more_repeats: bool) -> bool:
    shop_str = str(shop_id)
    for i in range(floor(len(shop_str) / 2)):
        substr = shop_str[0:i]
        if len(shop_str) % (i + 1) == 0:
            current = shop_str
            matched_count = 0
            while len(current) > 0:
                if current.startswith(substr):
                    matched_count += 1
                    current = current[i + 1:]
                    return matched_count >= 2 if more_repeats else matched_count == 2
    return False


def get_invalid_ids_from_ranges(ranges, more_repeats=False) -> int:
    invalid_sum = 0

    for possible_range in ranges:
        range_start, range_end = possible_range.split("-")
        if range_start.startswith("0") or range_end.startswith("0"):
            continue
        for current_id in range(int(range_start), int(range_end)):
            if get_invalid(current_id, more_repeats):
                invalid_sum += current_id

    return invalid_sum


start = time.time()
task1Sum = get_invalid_ids_from_ranges(data.split(","))
print("The sum of the invalid IDs is {}, calculated in {:.2f}ms".format(task1Sum, (time.time() - start) * 1000))

start = time.time()
task2Sum = get_invalid_ids_from_ranges(data.split(","), more_repeats=True)
print("The sum of the invalid IDs that appear at least twice is {}, calculated in {:.2f}ms".format(task2Sum, (time.time() - start) * 1000))
