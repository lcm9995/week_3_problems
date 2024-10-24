def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        if head.next.next == None:
            if n == 1:
                head.next = None
                return head
            else:
                return head.next
        counter = head
        sze = 1
        while counter.next is not None:
            sze +=1
            counter = counter.next
        k = 1
        curr = head
        if (sze-n) == 0:
            return head.next
        while k < (sze-n) and curr.next is not None:
            curr = curr.next
            k+=1
        curr.next = (curr.next).next
        return head