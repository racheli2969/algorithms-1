from typing import Optional

class Node:
    """Node class for binary tree"""
    def __init__(self, value):
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None


def print_mermaid(node: Optional[Node], node_id: str = "t") -> None:
    """
    Prints a binary tree in Mermaid format for visualization.
    
    Parameters:
    - node: The root node of the tree (or subtree)
    - node_id: The identifier for the current node (default "t" for root)
    
    Mermaid Syntax Rules:
    - Each node is printed as: id((value))
    - Edges are printed as: parent --> child
    - Empty nodes are shown as: id(( ))
    
    Example:
    For a tree:      10
                    /  \
                   5    15
                  /
                 3
    
    Output:
    graph TD
        t((10))
        t --> tl((5))
        t --> tr((15))
        tl --> tll((3))
        tl --> tlr(( ))
    """
    if node is None:
        return
    
    # Print the root node separately (only once)
    if node_id == "t":
        print("graph TD")
    
    # Print current node
    print(f"    {node_id}(({node.value}))")
    
    # Handle left child
    if node.left is not None:
        left_id = node_id + "l"
        print(f"    {node_id} --> {left_id}")
        print_mermaid(node.left, left_id)
    elif node.right is not None:
        # If left is None but right exists, print empty left node
        left_id = node_id + "l"
        print(f"    {node_id} --> {left_id}")
        print(f"    {left_id}(( ))")
    
    # Handle right child
    if node.right is not None:
        right_id = node_id + "r"
        print(f"    {node_id} --> {right_id}")
        print_mermaid(node.right, right_id)
    elif node.left is not None:
        # If right is None but left exists, print empty right node
        right_id = node_id + "r"
        print(f"    {node_id} --> {right_id}")
        print(f"    {right_id}(( ))")


# ===== Example Usage =====
if __name__ == "__main__":
    # Example 1: Simple balanced tree
    #       10
    #      /  \
    #     5    15
    #    / \   / \
    #   3   7 12  20
    
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)
    
    print("Example 1: Balanced Tree")
    print("=" * 50)
    print_mermaid(root)
    print()
    
    # Example 2: Tree with missing children
    #       10
    #      /  \
    #     5    15
    #    /      \
    #   3        20
    
    root2 = Node(10)
    root2.left = Node(5)
    root2.right = Node(15)
    root2.left.left = Node(3)
    root2.right.right = Node(20)
    
    print("\nExample 2: Tree with Missing Children")
    print("=" * 50)
    print_mermaid(root2)
    print()
    
    # Example 3: Skewed tree (left-heavy)
    #       10
    #      /
    #     5
    #    /
    #   3
    
    root3 = Node(10)
    root3.left = Node(5)
    root3.left.left = Node(3)
    
    print("\nExample 3: Left-Skewed Tree")
    print("=" * 50)
    print_mermaid(root3)
    print()
    
    print("\n" + "=" * 70)
    print("Copy the output above to: https://www.mermaidonline.live/mermaid-to-svg")
    print("=" * 70)
