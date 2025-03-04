class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr:
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, ' -> ')
            curr = curr.next
        print()


linked_list = LinkedList()
list_node = ListNode(3)
list_node.next = ListNode(4)
list_node.next.next = ListNode(5)

print(linked_list.head.val)
linked_list.remove(0)
print(linked_list.head.val)


linked_list.head = list_node
print(linked_list.head.val)

linked_list.insertEnd(7)

print(linked_list.tail.val)
