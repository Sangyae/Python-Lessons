set1 = {1,2,3,4}

print({i*i for i in set1})

squares = set()
for i in set1:
    squares.add(i*i)
print(squares)

name = "Bibek"
unique_characters = {char for char in name}
print(unique_characters)