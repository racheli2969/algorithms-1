import random
from typing import Optional 

class Node:
    def __init__(self, value):
        self.value = value
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None
        self.parent : Optional[Node] = None

    def print(self):
        if self.left:
            self.left.print()
        print(self.value, ", ", sep="", end="")
        if self.right:
            self.right.print()

    def print_indented(self, indent="", side=""):
        if self.right:
            if side == "left" or side=="":
                next_indent = indent+"   ┃"
            else:
                next_indent = indent[:-1]+"    ┃"
            self.right.print_indented(next_indent,side="right")

        current_indent=""
        if side=="left":
            current_indent=indent[:-1]+"┗"
        elif side=="right":
            current_indent=indent[:-1]+"┏"
        else:
            current_indent=""
        print(F"{current_indent}{self.value}")

        if self.left:
            if side == "right" or side=="":
                next_indent = indent+"   ┃"
            else:
                next_indent = indent[:-1]+"    ┃"
            self.left.print_indented(next_indent,side="left")


class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key

    def search_or_insert(self, value) -> Node:
        x = self.root
        y : Optional[Node] = None
        while x is not None:
            y = x
            if value == x.value:
                return x
            if self.key(value) > self.key(x.value):
                x = x.right
            else:
                x = x.left
        new_node = Node(value)
        if y is None:
            # the tree was empty
            self.root = new_node
        elif self.key(value) > self.key(y.value):
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y
        return new_node

    def insert(self, value):
        x = self.root
        y : Optional[Node] = None
        while x is not None:
            if value == x.value:
                # if the value is already in the tree, ignore
                return
            y = x
            if self.key(value) > self.key(x.value):
                x = x.right
            else:
                x = x.left
        
        new_node = Node(value)
        if y is None:
            # the tree was empty
            self.root = new_node
            return
        assert(value != y.value)
        if self.key(value) > self.key(y.value):
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y

    def print(self):
        if self.root:
            self.root.print()
        print() # print an empty line

    def print_indented(self):
        if self.root:
            self.root.print_indented()
    def print_indented(self):
        if self.root:
            self.root.print_indented()


# Example usage and tests:
if __name__ == "__main__":
    # Test 1: Simple integers with default key
    print("Test 1: Simple integers")
    tree1 = Tree()
    for value in [5, 3, 7, 1, 4, 6, 9]:
        tree1.insert(value)
    print("Tree structure:")
    tree1.print_indented()
    print("\nInorder: ", end="")
    tree1.print()
    
    # Test 2: Strings sorted by length using key function
    print("\n\nTest 2: Strings sorted by length")
    tree2 = Tree(key=lambda x: len(x))
    for word in ["apple", "hi", "banana", "cat", "elephant"]:
        tree2.insert(word)
    print("Tree structure:")
    tree2.print_indented()
    print("\nInorder: ", end="")
    tree2.print()
    
    # Test 3: Tuples sorted by second element
    print("\n\nTest 3: Tuples sorted by second element")
    tree3 = Tree(key=lambda x: x[1])
    for item in [(1, 5), (2, 3), (3, 7), (4, 1), (5, 6)]:
        tree3.insert(item)
    print("Tree structure:")
    tree3.print_indented()
    print("\nInorder: ", end="")
    tree3.print()
