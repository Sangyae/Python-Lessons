omlet = {'2eggs', 'paper','salt'}
boiled_egg = {'2eggs'}

is_subset = boiled_egg.issubset(omlet)
print("Is subset of omlet?", is_subset)

is_subset2 = omlet.issubset(boiled_egg)
print("Is subset of boiled_egg", is_subset2)

is_superset = boiled_egg.issuperset(omlet)
print("Is superset of omlet?", is_superset)