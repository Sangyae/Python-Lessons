users = ['bibek','Tamang','Sangyae']

Data = ['bibek','43','Tamang']

emptylist = []

print("bibek" in emptylist)

print(users[0])
print(users[-1])

print(users.index('Sangyae'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(Data))

users.append('gaming')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert','Jimmey'])   
print(users)

# users.extend(Data)
# print(users)

users.insert(0,'Bob')
print(users)

users[2:2] = ['Eddie','Mahat']
print(users)

users[1:3] = ['Robert','Hello']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

Data.clear()
print(Data)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [2, 4, 65, 7, 9]
nums.reverse()
print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

#Tuples

mytuple = tuple((2, "Tamang", True))

anothertuple = (1, 2, 3, 4)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(*one, two, Hey) = anothertuple
print(one)
print(two)
print(Hey)

print(anothertuple.count(1))