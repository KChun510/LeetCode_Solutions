#Link lst constructor
class Link:
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
 def reverseList(self, head):
     prev = None
     curr = head

      while curr:
        nexxt = curr.next
        #Changeing direction of pointer
        curr.next = prev
        prev = curr
        curr = nexxt
            
      return prev
