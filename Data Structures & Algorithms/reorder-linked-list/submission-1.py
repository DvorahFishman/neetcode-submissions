# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr_left = head
        curr_right = prev
        while curr_left and curr_right:
            temp_left = curr_left.next
            curr_left.next = curr_right
            curr_left = temp_left
            temp_right = curr_right.next
            curr_right.next = curr_left
            curr_right = temp_right
