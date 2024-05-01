class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_linked_list(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end="->")
            curr = curr.next
        print(None)

    def append_at_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_duplicate(self):

        if self.head is None:   # if the head is empty
            return None

        unique_node = set()
        current_node = self.head
        unique_node.add(current_node.val)

        while current_node.next is not None:
            if current_node.next.val in unique_node:    # duplicate found
                current_node.next = current_node.next.next  # remove duplicates
                self.length -= 1    # decrease length
            else:
                unique_node.add(current_node.next.val)  # if not duplicate add to the unique_node
                current_node = current_node.next    # update current for the next
            # update tail to the last node
            self.tail = current_node


new_linked_list = LinkedList()
new_linked_list.append_at_end(1)
new_linked_list.append_at_end(2)
new_linked_list.append_at_end(1)
new_linked_list.append_at_end(3)
new_linked_list.append_at_end(4)
new_linked_list.append_at_end(1)

print("Given Linked List")
new_linked_list.print_linked_list()

print("after removing duplicates")
new_linked_list.remove_duplicate()
new_linked_list.print_linked_list()


# def remove_duplicates(self):
#     unique_node = set()
#     curr_node = self.head
#     prev_node = None
#
#     while curr_node is not None:
#         if curr_node.val in unique_node:
#             prev_node.next = curr_node.next
#             curr_node = curr_node.next
#         else:
#             unique_node.add(curr_node.val)
#             prev_node = curr_node
#             curr_node = curr_node.next
#     return unique_node
