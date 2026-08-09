animalList = [('a', 'apes'), ('b', 'bear'), ('c', 'cat')]
animals = {item[0]: item[1] for item in animalList}

print(animals)

animals = {key: value for key, value in animalList}
print(animals)

animals.items()
list(animals.items())
print([{'letters': key, 'name' : value} for key, value in animals.items()])

