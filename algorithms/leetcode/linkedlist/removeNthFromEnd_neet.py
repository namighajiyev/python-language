from list_helper import createList, printList

class Solution:
    def removeNthFromEnd(self, head, n: int):
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length+=1
        if length == 1:
            return None
        
        indx=length-n +1
        
        if indx == 1:
            return head.next
        
        temp = head
        while indx - 2 > 0:
            temp = temp.next
            indx-=1
        if temp.next:
            temp.next = temp.next.next
        return head
            
        
sol = Solution();
head =createList([1,2])       
result =sol.removeNthFromEnd(head,1)
printList(result)