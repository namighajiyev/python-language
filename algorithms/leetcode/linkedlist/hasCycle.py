from collections import defaultdict
from list_helper import createList, printList


class Solution:
    def hasCycle(self, head):
        visited=defaultdict(lambda:False)
        while head:
            if visited[head]:
                return False
            head = head.next
        return head is not None
    
sol = Solution()
        
        