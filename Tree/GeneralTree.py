class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("Acer"))
    laptop.add_child(Treenode("Dell"))
    laptop.add_child(Treenode("Hp"))

    cell_phone = Treenode("Cell Phone")
    cell_phone.add_child(Treenode("Redmi"))
    cell_phone.add_child(Treenode("Realme"))
    cell_phone.add_child(Treenode("iPhone"))

    tv = Treenode("Television")
    tv.add_child(Treenode("Samsung"))
    tv.add_child(Treenode("LG"))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    return root
if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()