#Covering few basics 
#Not covering things like basic loop syntax print etc.

#For range loop 
words = ['cat', 'window', 'defenestrate']

for w in words:
	print(w, len(w))


#List and its Operations
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#Count elements 
print(fruits.count('apple'))
print(fruits.count('tangerine'))

#Finding index
print(fruits.index('banana'))
print(fruits.index('banana', 4)) #Find next banana @ pos 4

fruits.reverse()
print(fruits)

#Append
fruits.append('grape')
print(fruits)

#Sorting
fruits.sort()
print(fruits)

#Pop
print(fruits.pop())

#List comprehensions 
squares = []
for x in range(10):
	squares.append(x**2)

print(squares)

#Another way
squares1 = list(map(lambda x: x**2, range(10)))
print(squares1)

squares2 = [x**2 for x in range(10)]
print(squares2)