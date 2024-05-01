class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtFirst(list: Node, newValue: int) -> Node:

    new_node = Node(newValue)

    new_node.next = list
    list = new_node

    return list


list = Node(3)
list.next = Node(7)
list.next.next = Node(11)

print("Initial Linked List")

current = list
while current:
    print(current.data, end="->")
    current = current.next
print(None)


print("Linked List after insertion")

initial_list = insertAtFirst(list, 0)

current = initial_list

while current:
    print(current.data, end="->")
    current = current.next
print(None)

