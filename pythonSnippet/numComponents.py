class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def numComponents(head, G):
    num_connected = 0
    set_g = set(G)
    while head:
        if head.val not in set_g:
            head = head.next
            continue
        while head and head.val in set_g:
            head = head.next
        num_connected += 1
    return num_connected

ll = Node(0)
head = ll
ll.next = Node(1)
ll = ll.next
ll.next = Node(2)
ll = ll.next
ll.next = Node(3)
numComponents(head, [0, 1, 3])