# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if (head == None):
        return None
    if (head.next == None):
        return head
    tmpHead = head
    tmpNext = head.next.next
    head = head.next
    head.next = tmpHead
    head.next.next = tmpNext
    currentNode = head.next.next
    while (currentNode != None):
        if (currentNode.next == None):
            return head
        tmpVal = currentNode.val
        currentNode.val = currentNode.next.val
        currentNode.next.val = tmpVal
        currentNode = currentNode.next.next
    return head

n = 11
listNodeArr = []
for i in range(n):
    listNodeArr.append(ListNode(i+1))
for i in range(n):
    node = listNodeArr[i]
    if (i != n-1):
        node.next = listNodeArr[i+1]
result = swapPairs(listNodeArr[0])
valArr = []
while (result != None):
    valArr.append(result.val)
    result = result.next
print(valArr)