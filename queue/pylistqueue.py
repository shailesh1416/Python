# implementing queue using python list

class Queue:
    # Initialize the queue
    def __init__(self):
        self.items = list()
        self.size = 0

    # Returns the length of queue
    def length(self):
        return len(self.items)

    # Check if list is empty
    def isEmpty(self):
        return self.length() == 0

    # Add a new item to the list
    def enqueue(self, item):
        self.items.append(item)
        self.size += 1

    # Removes an item form the start of list
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
            self.size -= 1
        else:
            print("Queue is empty")
            return -1

    def draw(self):
        print(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.draw()
    q.dequeue()
    q.dequeue()
    q.draw()
    print(q.length())
    print(q.isEmpty())
