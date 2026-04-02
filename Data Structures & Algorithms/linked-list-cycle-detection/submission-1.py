# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while True:
            if fast.next == None or fast.next.next == None:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            

        return False

        