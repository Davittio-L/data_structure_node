#Practicing Data Struicturing
"""Basic Node that contains data and one link to another node. The node's data will be specified when creating the node and immutable."""

class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node