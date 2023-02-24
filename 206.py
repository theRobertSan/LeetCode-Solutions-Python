from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            cur = head
            head = head.next
            cur.next = dummy.next
            dummy.next = cur

        return dummy.next
