class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_node(node):

    # the value of the node to be deleted is overwritten by the value of its next node.
    node.data = node.next.data
    # Then, the next pointer of the given node is updated to skip over the next node and point to the node
    node.next = node.next.next

    return node


def print_node(node):
    temp = node
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print(None)


head = Node(4)
head.next = Node(5)
head.next.next = Node(1)
head.next.next.next = Node(9)

print("Given Node")
print_node(head)

print("after deleting the node")
# Find the node with the value 5 and delete it
node_to_delete = head.next
delete_node(node_to_delete)