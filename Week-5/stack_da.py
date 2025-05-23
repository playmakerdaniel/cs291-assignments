# Name: Daniel Burrows
# OSU Email: burrdani@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 Linked List and ADT Implementation
# Due Date: 05/05/2025
# Description: This assignment comprises of 5 parts. In the first part, you will complete the implementation of a Singly Linked List data structure.
# In part 2, you will implement the Stack ADT using your Dynamic Array from Assignment 2. For part 3, you will implement the Queue ADT using your Static Array from Assignment 1. For parts 4 and 5, you will again implement the Stack and Queue ADTs, but by using the Singly Linked Nodes


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        # Just add the value to the end of the dynamic array
        self._da.append(value)

    def pop(self) -> object:
        # Save the top value, remove it, then return it
        value = self._da[self._da.length() - 1]
        self._da.remove_at_index(self._da.length() - 1)
        return value

    def top(self) -> object:
        if self.is_empty():
            raise StackException()

        return self._da[self._da.length() - 1]


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
