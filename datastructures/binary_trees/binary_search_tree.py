# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of binary
# search tree
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#    - BST invariant:
#      + Nodes in the left subtree are smaller
#        than nodes in the right subtree
#      + The parent node is larger than all nodes
#        in the left subtree and small than all
#        nodes in the right subtree
# -----------------------------------------------

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.info)
logger = logging.getLogger()

class Node():
    def __init__(self, leftChild=None, rightChild=None, \
        parent=None, value=None):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent
        self.value = value


class BinarySearchTree():
    def __init__(self):
        self.root = None


    def insert_node(self, value, root):
        # Tree is empty/has no nodes 
        if self.root == None:
            logger.info("Tree was empty.")
            self.root = Node(None, None, self.root, value)
            return
        
        # Tree is not empty
        else:
            if value == root.value:
                logger.info(f"Cannot insert {value}, node already exists!")
                return
            elif value < root.value:
                if root.leftChild != None:
                    self.insert_node(root.leftChild, value)
                else:
                    root.leftChild = Node(None, None, root, value)
                    logger.info(f"Node {value} inserted!")
            else:
                if root.rightChild != None:
                    self.insert_node(root.rightChild, value)
                else:
                    root.rightChild = Node(None, None, root, value)
                    logger.info(f"Node {value} inserted!")
        
        return


    def find_node(self, value, node):

        ret = None

        # Tree is empty/has no nodes
        if self.root == None:
            logger.info(f"The tree is empty!")
        
        # Tree is not empty
        else:
            if value == node.value:
                ret = node
            elif value < node.value and node.leftChild != None:
                self.find_node(value, node.leftChild)
            elif value > node.value and node.rightChild != None:
                self.find_node(value, node.rightChild)

        return ret


    def remove(self, node):
        # Case 1: Leaf node
        if node.leftChild == None and \
            node.rightChild == None:
            del(node)

        # Case 2: Has leftsubtree
        elif node.leftChild != None and \
            node.rightChild == None:
            node.parent.leftChild = node.leftChild

        # Case 3: Has rightsubtree
        elif node.leftChild == None and \
            node.rightChild != None:
            node.parent.rightChild = node.rightChild

        # Case 4: Has both left and right subtrees
        # Successor - smallest node in right subtree 
        # OR largest node in left subtree
        


    def remove_node(self, value):
        # Tree is empty/has no nodes
        if self.root == None:
            logger.info(f"The tree is empty!") 

        # Tree is not empty
        else:
            node = self.find_node(value)
            self.remove(node)
        
        return


    def preorder_traversal(self):
        pass


    def inorder_traversal(self):
        pass


    def postorder_traversal(self):
        pass


    def print_tree(self):
        pass