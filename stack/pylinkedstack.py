# imlplementing stack using linked list

class Stack:
    # create an empty stack
    def __init__(self):
        self.size = 0
        self.top = None

    # return true if stack is empty or false otherwise
    def isEmpty(self):
        return self.size == 0

    # return the length of the stack
    def __len__(self):
        return self.size

    # return the top of the stack
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at empty stack"
        return self.top.data

    # Adding an item onto the top of stack

    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    # Remove and return top item from the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.data


class Node:
    def __init__(self, data, link):
        self.data = data
        self.next = link
