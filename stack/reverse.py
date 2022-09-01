# from pyliststack import Stack
from pylinkedstack import Stack

PROMPT = "Enter a number"
num = int(input(PROMPT))

# initialised a stack
stack = Stack()

# pushing value in stack until user inputs  a negative number
while num >= 0:
    stack.push(num)
    num = int(input(PROMPT))

# reversing the values form stack
while len(stack) > 0:
    print(stack.pop())
