# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    #base case
    if (head is None or head.next is None):
        return head
    
    #recursive step
    tmp = head
    head = reverseList(head.next)
    tmp.next.next = tmp
    tmp.next = None
    return head

n = 11
listNodeArr = []
for i in range(n):
    listNodeArr.append(ListNode(i+1))
for i in range(n):
    node = listNodeArr[i]
    if (i != n-1):
        node.next = listNodeArr[i+1]
result = reverseList(listNodeArr[0])
valArr = []
while (result != None):
    valArr.append(result.val)
    result = result.next
print(valArr)