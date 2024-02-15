n = int(input())
usage_ranges = []

for _ in range(n):
    hours_range_str = input().split(',')
    hours_range = [int(hour) for hour in hours_range_str]
    usage_ranges.append(hours_range)


# TODO: Define function to find the shutdown range given the number of ranges and the list of usage ranges
def find_shutdown_range(n, usage_ranges):
    only_list = [item for sublista in usage_ranges for item in sublista]
    min_valor = min(only_list)
    max_valor = max(only_list)
    unused_range = f'{max_valor},{min_valor}'

    return unused_range

shutdown_range = find_shutdown_range(n, usage_ranges)

print(shutdown_range)
