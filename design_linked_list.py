class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        # self.head.next = self.tail
        # self.tail.prev = self.head

    def get(self, index: int) -> int:
        index_node = self.head.next
        for i in range(index):
            if i == index:
                return index_node.val
            elif index_node:
                index_node = index_node.next

        return -1

    def addAtHead(self, val: int) -> None:
        self.head.prev = ListNode(val)
        self.head.prev.next = self.head
        self.head = self.head.prev
        print(self.head.val)
        print(self.head.next.val)

        return True

    def addAtTail(self, val: int) -> None:
        return True

    def addAtIndex(self, index: int, val: int) -> None:

        return True

    def deleteAtIndex(self, index: int) -> None:

        return True

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)