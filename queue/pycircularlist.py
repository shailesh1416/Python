from myarray import Array


class Queue:
    # Initialise a queue with a given size
    def __init__(self, max_size):
        self.items = Array(max_size)
        self.size = 0
        self.front = 0
        self.back = -1

    # Return the occupied length of queue
    def length(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == len(self.items)

    def __len__(self):
        return self.size

    # Enqueue an item into the queue

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue in a full queue"
        max_size = len(self.items)
        self.back = (self.back+1) % max_size
        self.items[self.back] = item
        self.items += 1

    # Dequeue and increment the front

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self.items[self.front]
        maxSize = len(self.items)
        self.front = (self.front+1) % maxSize
        self.size -= 1
        return item

    # prints item in list
    def draw(self):
        for i in self.items:
            print(i, end=' ')
        print()


q = Queue(4)

q.enqueue(1)
q.draw()
q.enqueue(2)
q.draw()
q.enqueue(3)
q.draw()
q.dequeue()
q.draw()
q.enqueue(4)
q.draw()
q.enqueue(5)
q.draw()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.draw()
q.dequeue()
q.draw()
q.enqueue("A")
q.draw()
q.enqueue("B")
q.draw()
q.dequeue()
q.draw()
