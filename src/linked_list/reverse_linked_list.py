class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):# Reverses a singly linked list
    prev = None # Previous node
    current = head # Current node
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node
    
    return prev  # New head of the reversed list

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else " -> None\n")
        current = current.next

# Test the function
if __name__ == "__main__":
    # Test case 1: Normal list with multiple elements
    print("Test case 1: [1, 2, 3, 4, 5]")
    multi_node_list_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print("Original list:")
    print_list(multi_node_list_head)

    reversed_multi_list = reverse_linked_list(multi_node_list_head)
    print("Reversed list:")
    print_list(reversed_multi_list)
    print()

    # Test case 2: Single element list
    print("Test case 2: [42]")
    single_node_list_head = ListNode(42)

    print("Original list:")
    print_list(single_node_list_head)

    reversed_single_list = reverse_linked_list(single_node_list_head)
    print("Reversed list:")
    print_list(reversed_single_list)
    print()

    # Test case 3: Two element list
    print("Test case 3: [1, 2]")
    two_node_list_head = ListNode(1, ListNode(2))

    print("Original list:")
    print_list(two_node_list_head)

    reversed_two_list = reverse_linked_list(two_node_list_head)
    print("Reversed list:")
    print_list(reversed_two_list)
    print()

    # Test case 4: Empty list
    print("Test case 4: []")
    empty_list_head = None

    print("Original list:")
    if empty_list_head is None:
        print("None")
    else:
        print_list(empty_list_head)

    reversed_empty_list = reverse_linked_list(empty_list_head)
    print("Reversed list:")
    if reversed_empty_list is None:
        print("None")
    else:
        print_list(reversed_empty_list)
    print()

    # Test case 5: Large list
    print("Test case 5: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    large_list_head = ListNode(1)
    current = large_list_head
    for i in range(2, 11):
        current.next = ListNode(i)
        current = current.next

    print("Original list:")
    print_list(large_list_head)

    reversed_large_list = reverse_linked_list(large_list_head)
    print("Reversed list:")
    print_list(reversed_large_list)