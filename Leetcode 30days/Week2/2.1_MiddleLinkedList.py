# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid,final = head,head
        while (final):
            final = final.next
            if (final):
                final = final.next
            else: break
            mid = mid.next
        return mid
