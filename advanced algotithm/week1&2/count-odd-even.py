def counter(number):
    even_count = 0
    odd_count = 0

    for current_numbers in number:
        if current_numbers % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

number = [1,2,3,4,5,6,7,8,9]
even, odd = counter(number)
print(f"Even numbers:{even}, Odd numbers:{odd}")