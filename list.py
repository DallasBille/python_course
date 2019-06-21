# import pdb; pdb.set_trace()
# breakpoint()

# these are lists (same as arrays, and manipulated the same as with ruby)
lists = [1,3,5,7,9]
mystringslist = ["strings","are","the","real","deal"]

# these are dictionaries, which are hashes, they are manipulated the same as ruby
dictionary = {"key1":123, "key2": [1,2,3], "key3": [4,5, "string"]}
# print(dictionary["key3"][2])

# tuples, a list that can't be changed. Has below sytax

tuple = (1,2,3)

# set, unordered collections of unique elements,  use "set" keyword.

aset = set()

aset.add("learning")
aset.add("python")
aset.add("it's")
aset.add("cool")

# prints {"learning", "python"} unordered

#  if, elif, and else example
first = 25
second = 50
if first > second:
     print("True Bitch")
elif first == second:
     print("elif Bitch")
else:
     print("Nope Bitch")

# Loops
# For Loop
list2 = [1,2,3,4,5,8,9]
dictionary2 = {"first": "Naomi", "second": "Dallas", "third": "Someone"}
for item in list2:
    print(item * 2)

for item in dictionary2:
    print(dictionary2[item])

# While Loop with .format()
number = 25
while number < 30:
    print("do it {}".format("baby!"))
    number = number +1

# Functions

def first_function(parameter):
    """
    THIS PRINTS OUT WHATEVER YOU PUT IN AS A PARAMETER
    """
    print(parameter)

# first_function("Fuuuuuuuck")

# Lambda and Filter Functions

list3 = "1,2,3,4,5,6,7,8,9"

print(list3.split(","))
