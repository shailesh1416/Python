class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self.count

    # Add given item to queue
    def enqueue(self, item):
        node = QueueNode(item)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1

    # Removes and teturn the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        node = self.head
        if self.head is self.tail:
            self.tail = None
        self.head = self.head.next
        self.count -= 1
        return node.item


# Storage class for creating the linked list node
class QueueNode:
    def __init__(self, item):
        self.item = item
        self.next = None
