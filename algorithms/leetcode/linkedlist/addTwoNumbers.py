from list_helper import createList, printList,ListNode

class Solution:
    def addTwoNumbers(self, l1, l2) :
        
        prev_sum = 0
        head= ListNode()
        temp = head;
            
        while l1 :
            prev_remider = 0 if prev_sum < 10 else 1
            #int((prev_sum - prev_sum%10) / 10)
            prev_sum = l1.val + l2.val + prev_remider
            val = prev_sum % 10
            temp.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            temp = temp.next
            
        if prev_sum > 9:
            # prev_remider = int((prev_sum - prev_sum%10) / 10)
            # temp.next = ListNode(prev_remider)
            temp.next = ListNode(1)
        
        return head.next

def test(arr1, arr2):
    l1 =createList(arr1)       
    l2 =createList(arr2)
    sol = Solution();
    result =sol.addTwoNumbers(l1,l2)
    printList(result)
    
test([2,4,3], [5,6,4])
test([9,9], [9,9])
test([9,9,9,9], [9,9,9,9])
test([0,9], [0,1])
test([9,9,9,9,9,9],[9,9,9,9,9,9])


