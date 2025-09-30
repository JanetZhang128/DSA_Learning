class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode(0)  # Dummy node to simplify edge cases
    current = dummy  # Pointer to build the new list

    while list1 and list2: # Traverse both lists
        if list1.value <= list2.value:  # Choose the smaller value
            current.next = list1 # Link to list1 node
            list1 = list1.next # Move to the next node in list1
        else:
            current.next = list2 # Link to list2 node
            list2 = list2.next# Move to the next node in list2
        current = current.next# Move the current pointer

    # Append remaining nodes
    current.next = list1 if list1 else list2 # Append any remaining nodes from either list

    return dummy.next

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else " -> None\n")
        current = current.next

# Test the function
if __name__ == "__main__":
    # Test case 1: Both lists have elements
    print("Test case 1: [1,2,4] and [1,3,4]")

    # Create first sorted list: 1 -> 2 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))

    # Create second sorted list: 1 -> 3 -> 4
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    print("List 1:")
    print_list(list1)
    print("List 2:")
    print_list(list2)

    merged = merge_two_sorted_lists(list1, list2)
    print("Merged list:")
    print_list(merged)
    print()

    # Test case 2: One empty list
    print("Test case 2: [] and [0]")
    list1 = None
    list2 = ListNode(0)

    merged = merge_two_sorted_lists(list1, list2)
    print("Merged list:")
    print_list(merged)
    print()

    # Test case 3: Both empty lists
    print("Test case 3: [] and []")
    list1 = None
    list2 = None

    merged = merge_two_sorted_lists(list1, list2)
    print("Merged list:")
    print_list(merged)
    print()

    # Test case 4: Different lengths
    print("Test case 4: [1,3,5,7] and [2,4]")
    list1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
    list2 = ListNode(2, ListNode(4))

    print("List 1:")
    print_list(list1)
    print("List 2:")
    print_list(list2)

    merged = merge_two_sorted_lists(list1, list2)
    print("Merged list:")
    print_list(merged)