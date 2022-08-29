# IMplementing bag ADT using linkd list

class Bag:
    def __init__(self):
        self._head = None
        self._size = 0

    # Returnd the number of itme in th Bag
    def __len__(self):
        return self._size

    # Determine if an item is contained in the list
    def __contains__(self, target):
        curNode = self._head
        while curNode != None and curNode.item != target:
            curNode = curNode.next

        if curNode is None:
            return "Not Found"
        else:
            return "Found"

    # traverse bag

    def traverse(self):
        curNode = self._head
        while curNode != None:
            print(curNode.item)
            curNode = curNode.next

    # add a new node to the bag
    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1
    # removes an instange of item from Bag

    def remove(self, item):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

        # The item has to be in bag to remove it
        assert curNode is not None, "The item must be in bag"

        # Unlink the item
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.item

    def __iter__(self):
        return _BagIterator(self._head)


class _BagListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    bag = Bag()d
    bag.add(11)
    bag.add(22)
    bag.add(36)
    bag.add(1)
    # bag.remove(4)

    print(bag._head.item)
    print(bag._size)
    print(bag.__contains__(11))
    bag.traverse()
