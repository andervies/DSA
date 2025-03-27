class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
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
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if self.head == self.tail:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

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

my_linked = MyLinkedList()
my_linked.addAtHead(2)
my_linked.addAtTail(3)
my_linked.addAtTail(4)

curr = my_linked.head
for i in range(4):

    print(curr.val)
    curr = curr.next

print(my_linked.get(1))