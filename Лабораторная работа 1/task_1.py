numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)
average_of_numbers = (sum(numbers[:none_index]) + sum(numbers[none_index + 1:])) / len(numbers)
numbers[none_index] = average_of_numbers

print("Измененный список:", numbers)
