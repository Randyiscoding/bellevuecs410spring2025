class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_bst(root, key):
    """
    Insert a new TreeNode with the given key into the binary search tree rooted at 'root'.
    Return the root of the modified tree.
    """
    if root is None:
        return TreeNode(key)
    elif key < root.val:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root
    pass

def find_max_heap(arr):
    """
    Given a max heap 'arr', return the maximum element (i.e., the root of the heap).
    If the heap is empty, return None.
    """
    return arr[0]  # Max-heap in an array is the max element at the root which is always the first element in an array
    pass

def is_full_binary_tree(root: TreeNode):
    """
    Check if the binary tree rooted at 'root' is a full binary tree.
    Return True if it is, otherwise return False.
    """
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
    else:
        if root.left is not None and root.right is not None:
            return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    pass

def get_tree_height(root: TreeNode):
    """
    Return the height of the binary tree rooted at 'root'.
    """
    if root is None:
        return 0
    left_height = get_tree_height(root.left)
    right_height = get_tree_height(root.right)

    return max(right_height, left_height) + 1
    pass