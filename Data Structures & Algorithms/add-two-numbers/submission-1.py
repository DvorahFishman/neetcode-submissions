# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        rest = 0

        dummy = ListNode(0) 
        curr = dummy

        while l2_curr or l1_curr or rest:
            val1 = l1_curr.val if l1_curr else 0
            val2 = l2_curr.val if l2_curr else 0
            
            curr_sum = val1 + val2 + rest
            curr_digit = curr_sum % 10
            rest = curr_sum // 10

            curr.next = ListNode(curr_digit)
            curr = curr.next

            if l1_curr:
                l1_curr = l1_curr.next
            if l2_curr:
                l2_curr = l2_curr.next
        return dummy.next





        