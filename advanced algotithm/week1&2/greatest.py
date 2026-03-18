def find_greatest(numbers):
    greatest = numbers[0]
    for current in numbers:
        if current > greatest:
            greatest = current
    return greatest

numbers = [3, 5, 2, 8, 1]
result = find_greatest(numbers)
print("The greatest number is :", result)

