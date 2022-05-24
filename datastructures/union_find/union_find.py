# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of disjoint
# set (union find) datastructure using arrays
# Note: This requires a bijective map to be 
# constructed before hand
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#   - Union
#   - Find
# -----------------------------------------------

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.info)
logger = logging.getLogger()

class UnionFind():
    def __init__(self, size):
        self.size = size
        self.num_sets = size
        self.set_size = []
        self.id = []

        for index in range(self.size):
            self.set_size.append(1)
            self.id.append(index)


    def union(self, node_1, node_2):
        root_1 = self.find(node_1)
        root_2 = self.find(node_2)

        if root_1 == root_2:
            logger.info(f"{node_1} and {node_2} belong to the same group - {root_1}")
            return
        
        if self.set_size[root_1] < self.set_size[root_2]:
            self.id[root_1] = root_2
            self.set_size[root_2] += self.set_size[root_1]
        else:
            self.id[root_2] = root_1
            self.set_size[root_1] += self.set_size[root_2]

        self.num_sets -= 1


    def find(self, node):
        # Find the set/group the node
        # belongs to
        root = node
        while(root != self.id[root]):
            root = self.id[root]
        
        # Path compression - gives amortized
        # constant time for find operations
        while(node != root):
            temp = self.id[node]
            self.id[node] = root
            node = temp

        return root


    def connected(self, node_1, node_2):
        return (self.find(node_1) == self.find(node_2))


    def _get_set_size(self, node):
        root = self.find(node)
        return self.set_size[root]


    def get_set_count(self):
        return self.num_sets