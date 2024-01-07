from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        sp, fp = head, head

        while True:
            fp = fp.next.next

            if fp is None or fp.next is None:
                sp.next = sp.next.next
                return head

            sp = sp.next
