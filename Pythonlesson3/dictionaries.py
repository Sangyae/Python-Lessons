#dictionaries

band = {
    "Vocals" : "Plants",
    "Guitar" : "Page"
}

band2 = dict(Vocals ="Plants", Guitar ="Page")

print(band)
print(band2)

print(type(band))
print(len(band))

# Access items

print(band["Vocals"])
print(band.get("Guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

# list of keys/values pairs as  tuples   
print(band.items())

#verify the key exists
print("Guitar" in band)
print("Triangle" in band)

#change values

band["Guitar"] = "Planks"
band.update({"bass": "JPJ"})
print(band)

# Remove values

print(band.pop("bass"))
print(band)

band["drums"] = "madal"
print(band)

print(band.popitem())
print(band)

#delete and clear

band["drums"] = "madal"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#copy dictionaries

# band2 = band # adds a reference
# print("bad copy!")
# band2["bibek"] = "tamang"
# print(band)


band2 = band.copy()
print("good copy!")
band2["bibek"] = "tamang"
print(band)
print(band2)

# or use dic() constructor function
band3 = dict(band)
print("good copy")
band3["sangyae"] = "gaming"
print(band)
print(band3)

#Nested dictionary

member1 ={
    "Name" : "Plant",
    "instrument" : "vocals"
}
member2 ={
    "Name" : "Page",
    "instrument" : "guitar"
}

band ={
    "member1" : member1,
    "member2" : member2
}

print(band)
print(band["member1"]["Name"])

#sets

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No duplicate allowed

nums = {1, 2, 2, 3, 4}
print(nums)

# True is dupe of 1 and False is dupe of 0

nums = {1, True, 2, 3, False, 0, 4}
print(nums)

#Check is value is in set
print(2 in nums)

#but you cannot refer to an element in the set  with an index position or key

# add a new elements in sets
nums.add(6)
print(nums)

#add elements from one set to another
morenums = {7, 8, 9}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples and directories, too

#merge two sets to create new sets
one = {1, 2, 3}
two = {4, 5, 6}

newset = one.union(two)
print(newset)

#Keep only the duplicates

one = {1, 2, 3}
two = {2, 3, 6}

one.intersection_update(two)
print(one)

#Keep everything except the duplicates

one = {1, 2, 3}
two = {2, 3, 6}

one.symmetric_difference_update(two)
print(one)