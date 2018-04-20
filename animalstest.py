animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
"""
Figuring out the ammount of elements in the dictionary animals
"""

# with a for loop
i = 0
for x in animals:
    i += len(animals[x])
print(i)

# with list comprehension
print(sum(len(x) for x in animals.values()))

# Prints key of longest element in animals
lengthOfLongestElement = 0
longestKey = ''

for keys in animals:
    
    if len(animals[keys]) > lengthOfLongestElement:
        lengthOfLongestElement = len(animals[keys])
        longestKey = keys

print(longestKey)

# Shamelessly stolen from other, provides key and length in one list
largestItem = ['', 0]

for key in animals:
    if len(animals[key]) > largestItem[1]:
        largestItem[0] = key
        largestItem[1] = len(animals[key])

print(largestItem)

# using an inbuilt to do this
print(max(animals.keys()))
