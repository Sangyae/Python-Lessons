empty_set = set()
print(empty_set)

fruits = {'mango', 'banana', 'apple', 'orange', 'banana'}
print(fruits)

color_list = {'blue', 'red', 'black'}
print(set(color_list))

if 'blue' in color_list:
    print("Yes there is blue in color_set.")
else:
    print("No there is no colour blue.")

set1 ={1,2,3,4}
set2 ={4,6,7}

result = any(num in set1 for num in set2)

if result:
    print("YEs there is at least one common number.")
else:
    print("NO there is not even a single common numberes.")

names = {'Bibek':24, 'Sapkota':22 }

if 'Bibek' in names:
    print("YEs there is bibek")
else:
    print("No sorry")

