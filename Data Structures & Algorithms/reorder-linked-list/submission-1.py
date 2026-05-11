class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
  
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    

        prev, curr = None, slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    
        ptr1 = head
        ptr2 = prev
       
        while ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = temp1

            ptr1 = temp1
            ptr2 = temp2
            