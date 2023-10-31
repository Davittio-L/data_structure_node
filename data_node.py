#Practicing Data Struicturing
"""Basic Node that contains data and one link to another node. The node's data will be specified when creating the node and immutable."""

class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    
    def get_value(self):
        return self.value
    
    def get_link_node(self):
        return self.link_node
    
    def set_link_node(self, link_node):
        self.link_node = link_node

james = Node("likes to snowboard")
john = Node("likes to ski")
stephanie = Node("does not like the snow")

stephanie.set_link_node(john)
james.set_link_node(stephanie)

stephanie_mood = james.get_link_node().get_value()
john_mood = stephanie.get_link_node().get_value()

print(stephanie_mood)
print(john_mood)