from myarray import Array
import random
# The constructor is called to create the array

valueList = Array(100)
print(valueList._size)
# Fill the array with random floating-point values
for i in range(valueList._size):
    valueList[i] = random.random()

# print the value, one per line
for value in valueList:
    print(value)
