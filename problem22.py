def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    sorted_numbers = sorted(numbers)
    mid_index = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    else:
        median = sorted_numbers[mid_index]

    return minimum, maximum, average, median

print(stats([3, 1, 4, 1, 5, 9, 2, 6]))