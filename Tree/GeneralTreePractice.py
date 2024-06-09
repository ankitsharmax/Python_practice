class Treenode:
    def __init__(self,name,designation):
        self.data = [name,designation]
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

    def print_tree(self,fashion="name"):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if fashion == "name":
            name = self.data[0]
            designation = ''
        elif fashion == "designation":
            name = ''
            designation = self.data[1]
        else:
            name = self.data[0]
            designation = '  (' + self.data[1] + ')'

        print(prefix + name + designation)
        if self.children:
            for child in self.children:
                child.print_tree(fashion)

def build_management_tree():
    root = Treenode("Nilu","CEO")

    cto = Treenode("Chinmay","CTO")
    inf_head = Treenode("Vishwa","Infrastructure Head")
    inf_head.add_child(Treenode("Dhaval","Cloud Manager"))
    inf_head.add_child(Treenode("Abhijit", "App Manager"))
    cto.add_child(inf_head)

    cto.add_child(Treenode("Aamir", "Application Head"))

    hr = Treenode("Gels","HR HEAD")
    hr.add_child(Treenode("Peter","Recruitment Manager"))
    hr.add_child(Treenode("Waqas","Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)

    return root

if __name__ == '__main__':
    root = build_management_tree()
    # root.print_tree("name")
    # root.print_tree("designation")
    root.print_tree("both")