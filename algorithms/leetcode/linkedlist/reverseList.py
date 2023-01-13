from list_helper import createList, printList

class Solution:
    def reverseList(self, head):
        p1, p2 = None, head
        while p2 is not None:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1
    
    
    """
   1->2->3->4 # p1 = None , p2 = 1 p3=2 #result 4->3->2->1->none
   1->None 2 ->3->4 # p1= 1, p2= 2 p3 =3
   2->1->None  3->4 #p1=2 p2=3 p3=4
   3->2->1->none 4 p1=3 p2=4 p3 = None
   4->3->2->1->None p1 =4 p2 =None p3 = None
   """""
   
sol = Solution()
printList(sol.reverseList(createList([1,2,3,4,5])))
printList(sol.reverseList(createList([1,2])))
printList(sol.reverseList(createList([])))


