# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


class LinkedList
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution
    def __init__(self, head):
        # empty list
        if head is None:
              return False

        slow = head
        fast = head

        # iterate to half of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversed the second half of the linked list
        cur = slow
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # compare the reversed second half with the first half
        ptr = head
        while prev:
            if prev.val == ptr.val:
                prev = prev.next
                ptr = ptr.next
            else:
                return False
        return True
        
            
