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

    def print_tree(self,level):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if level >= self.get_level() or self.parent == None:
            print(prefix + self.data, self.get_level())
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = Treenode("Global")

    india = Treenode("India")
    gujarat = Treenode("Gujarat")
    gujarat.add_child(Treenode("Ahmedabad"))
    gujarat.add_child(Treenode("Baroda"))
    karnataka = Treenode("Karnataka")
    karnataka.add_child(Treenode("Bangluru"))
    karnataka.add_child(Treenode("Mysore"))
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = Treenode("USA")
    new_jersey = Treenode("New Jersey")
    new_jersey.add_child(Treenode("Princeton"))
    new_jersey.add_child(Treenode("Trenton"))
    california = Treenode("California")
    california.add_child(Treenode("San Francisco"))
    california.add_child(Treenode("Mountain View"))
    california.add_child(Treenode("Palo Alto"))
    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(2)