# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        
        #While loop, creates a list copy of the Input lnked lst
        lst = []
        while head:
            lst += [head.val]
            head = head.next

        #Divide the list in half
        n = (int(len(lst) / 2))
        lst2 = lst[n :: ]
        
        #Special case
        if len(lst) == 1:
            return True
        
        #If given linked lst is even
        elif len(lst) % 2 != 0:
            lst3 = lst[0 : n + 1]
            #Compare Halfs
            if lst3 == lst2[::-1]:
                return True
            else:
                return False
        
        #If odd   
        else:
            lst3 = lst[0 : n]
            if lst3 == lst2[::-1]:
                return True
            else:
                return False

