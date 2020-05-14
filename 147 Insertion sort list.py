# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        if not head:
            return None
        
        pre = dummy
        curr = pre.next
        
        while curr:
            if curr.val < pre.val:
                ptr = dummy
                while (ptr and ptr.next and ptr.next.val < curr.val):
                    ptr = ptr.next
                
                ptr.next,curr.next,pre.next =  curr, ptr.next ,curr.next
                curr = pre.next
            else:
                pre = pre.next
                curr = pre.next
        return dummy.next
            
