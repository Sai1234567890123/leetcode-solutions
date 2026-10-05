# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        """
        Merges nodes between 0s in-place with O(1) auxiliary space.
        Modifies the values of existing nodes and rewires 'next' pointers.
        """
        # modify_ptr will point to the node where the current block's sum is stored.
        # Since the list starts with 0, head.next is the first non-zero node.
        modify_ptr = head.next
        curr = head.next
        
        running_sum = 0
        
        while curr:
            if curr.val != 0:
                running_sum += curr.val
                curr = curr.next
            else:
                # Reached the delimiter 0
                modify_ptr.val = running_sum
                running_sum = 0
                
                # If there are subsequent blocks (curr.next is not None),
                # link modify_ptr to the start of the next block.
                # Otherwise, terminate the list.
                if curr.next is not None:
                    modify_ptr.next = curr.next
                    modify_ptr = modify_ptr.next
                    curr = curr.next
                else:
                    modify_ptr.next = None
                    break
                    
        return head.next
