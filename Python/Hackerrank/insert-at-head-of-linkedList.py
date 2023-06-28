class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node):
    while node:
        node = node.next

def insertNodeAtTail(head, data):
    newNode = SinglyLinkedListNode(data)
    if llist == head:
        llist = newNode
    else:
        newNode.next = llist
        llist = newNode
    return llist
