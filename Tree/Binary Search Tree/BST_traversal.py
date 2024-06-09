# creating a binary node class
class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        elif data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # add data in right subtree
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


    def pre_order_traversal(self): #Root, Left, Right
        elements = []
        elements.append(self.data)

        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self): #Left, Right, Root
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        # add root node
        elements.append(self.data)

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,1,4,12,25,30,32,11,18]
    numbers_tree = build_tree(numbers)
    print("In order: ", numbers_tree.in_order_traversal())
    print("Pre order: ", numbers_tree.pre_order_traversal())
    print("Post order: ", numbers_tree.post_order_traversal())
