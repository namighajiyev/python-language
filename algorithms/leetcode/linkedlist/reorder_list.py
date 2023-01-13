from list_helper import createList, printList

class Solution:
    def reorderList(self, head) -> None:
        length=1
        tmp = head
        
        while tmp.next:
            length +=1
            tmp=tmp.next
        midIndex=(length//2) +1
        mid = head
        indx=1
        while indx < midIndex:
            mid=mid.next
            indx+=1
            
        current = head
        while midIndex < length:
            steps = length - midIndex
            end= mid
            while  steps > 0 :
                end = end.next
                steps -=1
            end.next = current.next
            current.next=end
            midIndex+=1
            current = end.next
        mid.next = None
            
head =createList([1,2,3,4,5,6,7,8,9])       
sol = Solution()
sol.reorderList(head)
printList(head)