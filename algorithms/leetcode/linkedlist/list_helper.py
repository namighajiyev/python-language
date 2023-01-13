# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
        
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
        