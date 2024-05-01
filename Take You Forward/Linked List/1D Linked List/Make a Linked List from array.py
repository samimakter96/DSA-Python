class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


def array_to_linked_list(arr):

    n = len(arr)

    head = Node(arr[0])
    temp = head

    for item in range(1, n):
        current_node = Node(arr[item])
        temp.next = current_node
        temp = temp.next

    return head


def display_linked_list(head):

    current = head
    while current:
        print(current.value, end="->")
        current = current.next
    print(None)


my_array = [1, 2, 3, 4, 5]
my_linked_list = array_to_linked_list(my_array)
display_linked_list(my_linked_list)

