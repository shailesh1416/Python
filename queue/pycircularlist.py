from myarray import Array


class Queue:
    # Initialise a queue with a given size
    def __init__(self, max_size):
        self.items = Array(max_size)
        self.size = 0
        self.front = 0
        self.back = -1
        self.max_size = max_size

    # Return the occupied length of queue
    def length(self):
        return self.size

    # Enqueue an item into the queue
    def enqueue(self, item):
        if self.size != self.max_size:
            if self.back < self.max_size-1:
                if self.back == self.front:
                    self.back
                self.back += 1
                self.size += 1
                self.items[self.back] = item
                print(
                    f'front = {self.front},back = {self.back}, size = {self.size}')
            else:
                self.back = 0
                self.size += 1
                self.items[self.back] = item
                print(
                    f'front = {self.front},back = {self.back}, size = {self.size}')

        else:
            print(self.front, self.back)
            print("Queue is full, enqueue to ")

    # Dequeue and increment the front

    def dequeue(self):
        if self.length() > 0:
            if self.front < self.max_size:
                temp = self.items[self.front]
                self.size -= 1
                self.items[self.front] = None
                if self.front + 1 == self.max_size:
                    self.front = 0
                else:
                    self.front += 1
                print(
                    f'front = {self.front},back = {self.back}, size = {self.size} dequeued = {temp}')
                return temp
            else:
                self.front = 0
                temp = self.items[self.front]
                self.items[self.front] = None
                self.size -= 1
                print(
                    f'front = {self.front},back = {self.back}, size = {self.size} dequeued = {temp}')
                return temp

        else:
            print("Queue is empty")
            return -1

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
