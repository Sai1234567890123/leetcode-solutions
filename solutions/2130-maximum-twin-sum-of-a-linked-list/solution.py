# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if not head or not head.next:
            return 0
        
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # At this point, 'slow' points to the start of the second half of the list.
        # Step 2: Reverse the second half of the linked list in-place
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 'prev' is now the head of the reversed second half
        # Step 3: Compute maximum twin sum by traversing both halves
        max_twin_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        # Optional Step: Restore the linked list if required by the caller (best practice)
        # We can reverse the second half again to leave the input unmodified:
        # curr, prev_restore = prev, None
        # while curr:
        #     next_node = curr.next
        #     curr.next = prev_restore
        #     prev_restore = curr
        #     curr = next_node

        return max_twin_sum
