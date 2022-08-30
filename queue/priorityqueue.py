# Implementation of unbounded priority queue ADT using a python list

class PriorityQueue:
    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        return len(self._qlist)

    def __len__(self):
        return len(self._qlist)

    # adds the given item to the queue
    def enqueue(self, item, priority):
        # create new instance of storage clas and append to the list
        entry = _PriorityQEntry(item, priority)
        self._qlist.append(entry)

    # Remove and return first item in the queue
    def dequeue(self):
        assert self.isEmpty(), "Cannot dequeue from an empty queue"
        # Find the entry with highest priority
        highest = self._qlist[0].priority
        for i in range(1, len(self)):
            if self._qlist[i] < highest:
                highest = self._qlist[i].priority
        entry = self._qlist.pop(highest)
        return entry


class _PriorityQEntry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
