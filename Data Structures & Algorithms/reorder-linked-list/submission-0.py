# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head , head.next

        #finding the splitting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        #reversing second linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        list1, list2 = head, prev
        while list2:
            temp1 , temp2 = list1.next , list2.next
            list1.next = list2
            list2.next = temp1
            list1 , list2 = temp1 , temp2


        
        