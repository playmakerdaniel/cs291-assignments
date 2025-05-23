# Name: Daniel Burrows
# OSU Email: burrdani@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 Linked List and ADT Implementation
# Due Date: 05/05/2025
# Description: This assignment comprises of 5 parts. In the first part, you will complete the implementation of a Singly Linked List data structure.
# In part 2, you will implement the Stack ADT using your Dynamic Array from Assignment 2. For part 3, you will implement the Queue ADT using your Static Array from Assignment 1. For parts 4 and 5, you will again implement the Stack and Queue ADTs, but by using the Singly Linked Nodes


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        # Create a new node that holds the value
        new_node = SLNode(value)

        # Link the new node to what was previously the first node
        new_node.next = self._head.next

        # Make the sentinel node point to the new node — it's now the first real element
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        # Start from the sentinel node
        current = self._head

        # Walk through the list until we find the end
        while current.next:
            current = current.next

        # Create a new node and link it as the last element
        current.next = SLNode(value)

    def insert_at_index(self, index: int, value: object) -> None:
        # Make sure the index is in a valid range
        if index < 0 or index > self.length():
            raise SLLException()

        # Start from the sentinel node
        current = self._head

        # Move to the node just before the target position
        for _ in range(index):
            current = current.next

        # Link in the new node
        new_node = SLNode(value)
        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index: int) -> None:
        # Make sure the index is in range
        if index < 0 or index >= self.length():
            raise SLLException()

        # Start at the sentinel
        current = self._head

        # Move to the node just before the one we want to remove
        for _ in range(index):
            current = current.next

        # Skip over the node we're removing
        current.next = current.next.next

    def remove(self, value: object) -> bool:
        # Start at the sentinel node
        current = self._head

        # Walk the list while we have a next node to inspect
        while current.next:
            if current.next.value == value:
                # Found a match, remove it by skipping over it
                current.next = current.next.next
                return True
            current = current.next

        # Value not found
        return False

    def count(self, value: object) -> int:
        # Start at the first real node
        current = self._head.next
        count = 0

        # Walk through the list, counting matches
        while current:
            if current.value == value:
                count += 1
            current = current.next

        return count

    def find(self, value: object) -> bool:
        # Start at the first actual node
        current = self._head.next

        # Look for a match
        while current:
            if current.value == value:
                return True
            current = current.next

        # Value not found in the list
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        # Check for invalid input
        if start_index < 0 or size < 0 or start_index + size > self.length():
            raise SLLException()

        # Start from the first real node
        current = self._head.next

        # Move to the node at start_index
        for _ in range(start_index):
            current = current.next

        # Build a new list and copy over 'size' elements
        new_list = LinkedList()
        for _ in range(size):
            new_list.insert_back(current.value)
            current = current.next

        return new_list


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
