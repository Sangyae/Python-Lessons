def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number **0.5) + 1):
        if number % i == 0:
            return False
    return True
    
def generate_prime_set(number):
    return {num for num in number if is_prime(num)}

number = {1,2,3,4,5,6,7,8,9,10}
prime_numbers = generate_prime_set(number)
print(prime_numbers)

