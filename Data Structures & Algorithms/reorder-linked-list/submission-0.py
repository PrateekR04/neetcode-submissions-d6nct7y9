class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # Step 1: Store nodes in array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        # Step 2: Reorder using two pointers
        i, j = 0, len(arr) - 1
        
        while i < j:
            arr[i].next = arr[j]
            i += 1
            
            if i == j:
                break
            
            arr[j].next = arr[i]
            j -= 1
        
        # Step 3: End the list
        arr[i].next = None

    
        