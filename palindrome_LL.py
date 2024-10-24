def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head.next is None:
            return True
        elif ((head.next).next is None):
            if head.val != head.next.val:
                return False
            else:
                return True
        n = 1
        end = head
        while end.next is not None:
            end = end.next
            n +=1
        front = head
        #stck = [0]*(int(ceil(n/2))+1)
        stck = []
        for i in range(0, n/2):
            stck.append(front.val)
            front = front.next
        if n == 3:
            if front.next.val == head.val:
                return True
            else:
                return False
        #for i in range():
        if (n%2 != 0 and n > 3):
            front = front.next
        while front is not None:
            temp = stck.pop()
            if front.val != temp:
                return False
            front = front.next
            #front = front.next
        return True