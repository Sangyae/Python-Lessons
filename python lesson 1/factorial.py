def factorail(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    return num * factorail(num-1)

num = int(input("Enter any integer numbers."))
fact = factorail(num)
print(fact)