# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    encounteredList = []
    node = head
    while node != None:
        if node.val in encounteredList:
            print(encounteredList)
            return True
        encounteredList.append(node.val)
        node = node.next
    return False

head = ListNode(1)
head.next = ListNode(2)
print(hasCycle(head))