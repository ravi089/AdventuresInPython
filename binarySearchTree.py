# Binary search tree in python.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def insert_helper(self, root, data):
        if not root:
            root = Node(data)
            return root
        if data > root.data:
            root.right = self.insert_helper(root.right, data)
        else:
            root.left = self.insert_helper(root.left, data)
        return root

    def inorder_helper(self, root):
        if not root:
            return
        self.inorder_helper(root.left)
        print (root, end=' ')
        self.inorder_helper(root.right)

    def search_helper(self, root, key):
        if not root:
            return False
        return (root.data == key) or self.contains_helper(root.left, key) or self.contains_helper(root.right, key)

    def delete_helper(self, root, key):
        if not root:
            return root
        if key < root.data:
            root.left = self.delete_helper(root.left, key)
        elif key > root.data:
            root.right = self.delete_helper(root.right, key)
        else:
            # Here we delete the node.
            # If no left/right child, delete node promoting other as parent.
            # this will cover the case of node with no children.
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # if both child exits, replace it's value with minimum in right
            # subtree. now delete that minimum value in subtree.
            temp = root.right
            inord_succ = root.right
            while inord_succ.left:
                inord_succ = inord_succ.left
            root.data = inord_succ.data
            root.right = self.delete_helper(root.right, root.data)
        return root
    
    def insert(self, data):
        self.root = self.insert_helper(self.root, data)

    def inorder(self):
        print ('[', end=' ')
        self.inorder_helper(self.root)
        print (']')

    def search(self, key):
        return self.contains_helper(self.root, key)

    def delete(self, key):
        self.delete_helper(self.root, key)
    
if __name__ == '__main__':
    t = Tree()
    t.insert(5)
    t.insert(2)
    t.insert(9)
    t.insert(7)
    t.insert(8)
    t.insert(4)
    t.insert(1)
    t.insert(3)
    t.insert(6)

    t.delete(9)
    t.delete(4)
    t.delete(1)
    t.delete(5)
    
    print ('inorder traversal')
    t.inorder()
