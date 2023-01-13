from collections import defaultdict
from list_helper import createList, printList
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
def createListWithRandom(arr, randoms):
    head = createList(arr)
    temp =head
    nodes = [temp]
    while temp and  temp.next:
        nodes.append(temp.next)
        temp =temp.next

    for i,random in enumerate(randoms):
        node = nodes[i]
        if node is not None:
            node.random = nodes[random] if random is not None else None
    return head

def buildNodesDict(head) :
    i = 0
    temp = head
    dict= {};
    dict[temp] = 0
    while temp.next:
        i+=1
        dict[temp.next] = i
        temp =temp.next
    return dict

def printListWithRandom(head):
    dict = buildNodesDict(head)
    values = []
    curr = head
    while curr :
        random_index = dict[curr.random] if curr.random else None
        values.append([curr.val,random_index])
        curr= curr.next
    print(values)
    
class Solution:
    def copyRandomList(self, head):
        dict = buildNodesDict(head)
        values = [head.val]
        randoms = [dict[head.random] if head.random is not None else None]
        while head.next:
            values.append(head.next.val)
            if head.next.random: 
                randoms.append(dict[head.next.random])
            else:
                randoms.append(None)
            head = head.next
        head = createListWithRandom(values, randoms) 
        return head
        
        

    
#[[3,null],[3,0],[3,null]]
head = createListWithRandom([3,3,3], [None, 0,None])  
printListWithRandom(head)
sol = Solution()
new_head = sol.copyRandomList(head)
printListWithRandom(new_head)

