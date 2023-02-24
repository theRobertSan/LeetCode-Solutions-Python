from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = fp = head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

            if sp == fp:
                # Cycle detected
                while head != sp:
                    head = head.next
                    sp = sp.next
                return sp

        return None
