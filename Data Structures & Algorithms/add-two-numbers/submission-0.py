# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head helps manage the result list easily
        dummy_head = ListNode()
        current_node = dummy_head
        carry = 0

        # Loop until both lists are done AND there's no carry left
        while l1 or l2 or carry:
            # Get values, using 0 if a list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and update carry for the NEXT loop
            total_sum = v1 + v2 + carry
            carry = total_sum // 10
            
            # Create a new node with the units digit
            current_node.next = ListNode(total_sum % 10)
            
            # Advance all pointers
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy_head.next
        