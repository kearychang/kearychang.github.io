# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        return head

    def reverseListRecur(head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        return head

n = 9
listNodeArr = []
for i in range(n):
    listNodeArr.append(ListNode(i+1))
for i in range(n):
    headNode = listNodeArr[i]
    headNode.next = listNodeArr[i+1]
result = reverseList(headNode)
resultRecur = reverseListRecur(headNode)
valArr = []
valArrResur = []
while (result != None):
    valArr.append(result.val)
    result = result.next
while (resultRecur != None):
    valArrResur.append(resultRecur.val)
    resultRecur = resultRecur.next
print(valArr)
print(valArrResur)