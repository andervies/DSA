# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nexxt = head.next
            head.next = prev
            prev = head
            head = nexxt

        return prev



linked_list = None
for i in range(1,6):
    linked_list = ListNode(i, linked_list)


def print_linked_list_vals(linked_list):
    while linked_list:
        print(linked_list.val)
        linked_list = linked_list.next

print_linked_list_vals(linked_list)


## Let's test our algorithm
soln = Solution()
print("Reversing the linked list above")
print_linked_list_vals(soln.reverseList(linked_list))



