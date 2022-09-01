# Implementing the stack ADT using python list

class Stack:
    # Initializing the stack with empty list
    def __init__(self):
        self.theitems = list()

    # returns the length of the stack
    def __len__(self):
        return len(self.theitems)

    # Checks wheather stack is empty
    def isEmpty(self):
        return len(self) == 0

    # peek at the top item of the stack
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.theitems[-1]

    # Pushes a value int the stack

    def push(self, value):
        self.theitems.append(value)

    # removes a value int the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self.theitems.pop()
