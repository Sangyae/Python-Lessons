set1 = [1,2,3,4,5,6,7,8,9,10]

result = {num for num in set1 if num % 2 == 0 }
print(result)

fruits = {'apple','banana', 'mango', 'grapes','kewi'}
result2 = {fruits.upper() for fruits in fruits if 'a' in fruits}
print(result2)