class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self): #Left, Root, Right
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # root note
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def search(self,value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def sum_elements(self):
        return sum(self.in_order_traversal())

    def delete_node(self,value):
        '''Find the maximum element in the left tree of the node you want to delete and replace with the max element.'''
        # if value in left tree
        if value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        # if value in right tree
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        # found value if node in value
        else:
            # no child
            if self.left is None and self.right is None:
                return None
            # only left child
            elif self.right is None:
                return self.left
            # only right child
            elif self.left is None:
                return self.right
            else:
                maxValue = self.left.find_max()
                self.data = maxValue
                self.left.delete_node(maxValue)

        return self

def build_binary_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 1, 4, 12, 25, 30, 32, 11, 18]
    numbers_tree = build_binary_tree(numbers)
    print("Inorder traversal", numbers_tree.in_order_traversal())
    print("12 in numbers_tree", numbers_tree.search(12))
    print("200 in numbers_tree", numbers_tree.search(200))
    print("Sum of all elements in numbers_tree", numbers_tree.sum_elements())
    print("Minimum element", numbers_tree.find_min())
    print("Maximum element", numbers_tree.find_max())
    print("Inorder traversal", numbers_tree.in_order_traversal())
    numbers_tree.delete_node(12)
    print("Deleting node 12:", numbers_tree.in_order_traversal())
    numbers_tree.delete_node(32)
    print("Deleting node 32:", numbers_tree.in_order_traversal())
    numbers_tree.delete_node(17)
    print("Deleting node 17:", numbers_tree.in_order_traversal())