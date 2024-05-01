class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_node_from_end(head, n):

    start = Node(0)
    start.next = head

    first = start
    slow = start

    for i in range(n):
        first = first.next

    while first.next != None:
        slow = slow.next
        first = first.next

    slow.next = slow.next.next

    return start.next


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.value, end="->")
        temp = temp.next
    print(None)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Given List")
print_linked_list(head)

remove = remove_node_from_end(head, 2)
print_linked_list(remove)
