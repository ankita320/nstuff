class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        h = dummy

        while list1 and list2:
            if list1.val > list2.val:
                h.next = list2
                list2 = list2.next
            else:
                h.next = list1
                list1 = list1.next
            h = h.next

        if list1:
            h.next = list1
        else:
            h.next = list2

        return dummy.next