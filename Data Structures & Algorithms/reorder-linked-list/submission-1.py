# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Cut the first half
        while curr:
            nxt_temp = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_temp
            
        # Step 3: Merge the two halves alternately
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

    
            