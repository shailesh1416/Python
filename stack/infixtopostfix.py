from pylinkedstack import Stack

precedence = ['(']

expression = '5+10*20+30'

operandStack = Stack()
operatorStack = Stack()

for char in expression:
    if char not in '+-*/':
        operandStack.push(char)
    elif char in '+-*/':
        if operatorStack.isEmpty():
            operatorStack.push(char)
        elif precedence.index(char) > precedence.index(operatorStack.top):
            operatorStack.push(char)
        elif precedence.index(char) < precedence.index(operatorStack.top):
            while not operatorStack.isEmpty() or precedence.index(char) > precedence.index(operatorStack.top):
                operatorStack.pop()
