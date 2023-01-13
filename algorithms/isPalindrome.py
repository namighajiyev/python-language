class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def createList(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    tail = head
    for i in range(1, len(arr)):
        tail.next = ListNode(arr[i])
        tail = tail.next
    return head

def printList(head):
    values = []
    curr = head
    while curr :
        values.append(curr.val)
        curr= curr.next
    print(values)

class Solution:
    def isPalindrome(self, head) -> bool:
        
        slow=head
        fast=head
        isOdd=True
        while fast.next is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
            slow =slow.next
            isOdd = not isOdd
        print(slow, isOdd)
        
        right = slow.next
        
        #if even include slow else not in reverse
        p1, p2 = None, head
        while p2 != slow:
            p3 = p2.next
            p1=p2
            p2=p3
        
        left = p2
        while right is not None:
            if left.val != right.val:
                return False
            left=left.next
            right = right.next
        
        return True
    