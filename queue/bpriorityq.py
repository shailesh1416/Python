from myarray import Array
from linkedlistqueue import Queue


class BPriorityQueue:
    def __init__(self, numLevel):
        self._qLevels = Array(numLevel)
        self._qSize = 0

        for i in range(numLevel):
            self._qLevels[i] = Queue()

    # Return True if queue is empty
    def isEmpty(self):
        return len(self) == 0

    # Retuens number of item in queue
    def __len__(self):
        return len(self._qSize)

    # Add the givn item to the queue
    def enqueue(self, item, priority):
        assert not self.isEmpty(), "Cannot dequeue from and empty queueu"
        # find first non empty queue
        i = 0
        p = len(self._qLevels)
        while i < p and not self._qLevels[i].isEmpty():
            i += 1
        return self._qlist[i].dequeue()
