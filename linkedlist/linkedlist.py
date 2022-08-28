class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def traversal(head):
    curnode = head
    while curnode is not None:
        print(curnode.data)
        curnode = curnode.next

# unordered linked-list => find a target


def unorderedSearch(head, target):
    curnode = head
    while curnode is not None and curnode != target:
        curnode = curnode.next
    return curnode is not None


def addItem(head, item):
    newNode = ListNode(item)
    newNode.next = head
    head = newNode
    return head


'''def remove(head, target):
    preNode = None
    curnode = head
    while curnode is not None and curnode.data != target:
        curnode = curnode.next
        preNode = curnode

    if curnode is not None:
        if curnode is head:
            head = curnode.next
        else:
            preNode = curnode.next
'''

if __name__ == '__main__':
    head = ListNode("India")
    n2 = ListNode("Pakistan")
    n3 = ListNode("Afganistan")
    n4 = ListNode("Turky")

    head.next = n2
    n2.next = n3
    n3.next = n4
    head = addItem(head, "Bangladesh")
    traversal(head)
