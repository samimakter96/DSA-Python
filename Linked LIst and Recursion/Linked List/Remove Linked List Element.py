# Define the ListNode class
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# Function to remove an element from the linked list
def remove_element(head, target):
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)

    dummy.next = head
    current = dummy  # Initialize a pointer to the dummy node

    # Iterate through the linked list
    while current.next:
        # Check if the next node contains the target value
        if current.next.value == target:
            # Adjust the pointers to skip the node with the target value
            current.next = current.next.next
        else:
            # Move to the next node in the linked list
            current = current.next

    # Return the modified linked list (excluding the dummy node)
    return dummy.next


# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Print the original linked list
current_node = head
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")

# Remove the element with the value 3
head = remove_element(head, 3)

# Print the modified linked list
current_node = head
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
