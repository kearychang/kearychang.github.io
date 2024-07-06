import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if (self.val is None):
            return ""
        else:
            s = ""
            tmp = self
            while (not tmp is None):
                s = s + str(tmp.val) + " "
                tmp = tmp.next
            return s

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoListsRecur(l1, l2, mergeL, mergeLHead):
        if (l1 is None and l2 is None):
            return mergeLHead
        if (not l2 is None and (l1 is None or (l2.val <= l1.val))):
            if (mergeL is None):
                mergeL = l2
                mergeLHead = mergeL
            else:
                mergeL.next = ListNode(l2.val)
                mergeL = mergeL.next
            return mergeTwoListsRecur(l1, l2.next, mergeL, mergeLHead)
        else:
            if (not mergeL):
                mergeL = l1
                mergeLHead = mergeL
            else:
                mergeL.next = ListNode(l1.val)
                mergeL = mergeL.next
            return mergeTwoListsRecur(l1.next, l2, mergeL, mergeLHead)
    mergeL = mergeTwoListsRecur(l1, l2, None, None)
    return mergeL

n = 9
listNodeArr, listNodeArr2 = [], []
for i in range(n):
    listNodeArr.append(ListNode(random.randint(0,100)))
    listNodeArr2.append(ListNode(random.randint(0,100)))
listNodeArr.append(None)
listNodeArr2.append(None)
headNode, headNode2 = listNodeArr[0], listNodeArr2[0]
tmp, tmp2 = headNode, headNode2
for i in range(n):
    headNode.next, headNode2.next = listNodeArr[i+1], listNodeArr2[i+1]
    headNode, headNode2 = headNode.next, headNode2.next
print(tmp)
print(tmp2)
m = mergeTwoLists(tmp, tmp2)
print(m)