class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addItem(self, item):
        newNode = ListNode(item)
        newNode.next = self.head
        self.head = newNode

    def traversal(self):
        curnode = self.head
        while curnode is not None:
            print(curnode.data)
            curnode = curnode.next

    # unordered linked-list => find a target
    def unorderedSearch(self, target):
        curnode = self.head
        while curnode is not None and curnode != target:
            curnode = curnode.next
        if curnode is None:
            return False
        return True

    def remove(self, target):
        preNode = None
        curnode = self.head
        while curnode is not None and curnode.data != target:
            curnode = curnode.next
            preNode = curnode

        if curnode is not None:
            if curnode is self.head:
                self.head = curnode.next
            else:
                preNode.next = curnode.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.addItem("India")
    llist.addItem("Pakistan")
    llist.addItem("Afganistan")
    llist.addItem("Iran")

    llist.remove('Afganistan')
    llist.traversal()
