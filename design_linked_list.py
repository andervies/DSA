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
        curr = self.head.next
        count = 0

        while curr :
            if count == index:
                return curr.val
            elif curr:
                curr = curr.next
                count += 1

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
        count = 0
        # Let curr trail behind the count since for a singly linked list we'd need the previous node before the indexth
        curr = self.head

        while curr and count < index:
            count += 1
            curr = curr.next


        if curr:
            new_node = ListNode(val)
            new_node.next = curr.next
            curr.next = new_node

            if new_node.next is None:
                self.tail = new_node



    def deleteAtIndex(self, index: int) -> None:
        count = 0
        # Let curr trail behind the count since for a singly linked list we'd need the previous node before the indexth
        curr = self.head

        while curr and count < index:
            count += 1
            curr = curr.next

        if curr and curr != self.tail:
            curr.next = curr.next.next

            if curr.next is None:
                self.tail = curr
            # if curr == self.tail:



    def print(self):
        curr = self.head.next
        while curr:
            print(' -> ', curr.val)
            curr = curr.next
        print()



my_linked = MyLinkedList()
my_linked.addAtHead(7)
my_linked.addAtHead(2)
my_linked.addAtHead(1)
my_linked.addAtIndex(3,0)
my_linked.print()
my_linked.deleteAtIndex(2)
my_linked.print()
my_linked.addAtHead(6)
my_linked.print()
my_linked.addAtTail(4)
my_linked.print()

print(f"getting index 4 {my_linked.get(4)}")

my_linked.addAtHead(4)
my_linked.print()
my_linked.addAtIndex(5,0)
my_linked.print()
my_linked.addAtHead(6)
my_linked.print()


print(my_linked.tail.val)
my_linked.deleteAtIndex(0)
print(my_linked.tail.val)

# ToDo: Assert that the tail pointer stays relatively consistent across all operations
