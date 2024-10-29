# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_list = 1
        curr = head
        mid = 0 

        while curr.next:
            len_list += 1
            curr = curr.next

        if len_list == 1:
            return None

        mid = len_list // 2

        i = 0
        curr = head
        while i <= mid:
            if i + 1 == mid:
                next_node = curr.next
                if next_node == None:
                    curr.next = None
                else:
                    curr.next = next_node.next
                break
            curr = curr.next
            i += 1
        
        return head
        
