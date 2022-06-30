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
#        in the left subtree and smaller than all
#        nodes in the right subtree
# -----------------------------------------------

import logging
import sys

from stacks.stack import Stack
from queues.queue import Queue

logging.basicConfig(stream=sys.stdout, level=logging.debug)
logger = logging.getLogger()

class Node():
    def __init__(self, leftChild=None, rightChild=None, value=None):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.value = value


class BinarySearchTree():
    def __init__(self):
        self.root = None


    def insert(self, value, root=None):
        # Tree is empty/has no nodes 
        if self.root == None:
            self.root = Node(None, None, value)
            return
        
        # Tree is not empty
        else:
            if root == None:
                # Start from the root node
                root = self.root
            
            if value == root.value:
                logger.info(f"Cannot insert {value}, node already exists!")
                return
            elif value < root.value:
                if root.leftChild != None:
                    self.insert(value, root.leftChild)
                else:
                    root.leftChild = Node(None, None, value)
                    logger.info(f"Node {value} inserted!")
            else:
                if root.rightChild != None:
                    self.insert(value, root.rightChild)
                else:
                    root.rightChild = Node(None, None, value)
                    logger.info(f"Node {value} inserted!")
        return 


    def insert_node(self, value):
        self.insert(value, self.root)
        return 


    def find_node(self, value, node=None):
        # Tree is empty/has no nodes
        if self.root == None:
            logger.info(f"The tree is empty!")
            return False
        # Tree is not empty
        else:
            if node == None:
                # Start from the root node
                node = self.root

            if value == node.value:
                logger.info(f"Found {value}")
                return True
            elif value < node.value and node.leftChild != None:
                return self.find_node(value, node.leftChild)
            elif value > node.value and node.rightChild != None:
                return self.find_node(value, node.rightChild)
            else:
                logger.info("Node not found!")
                return False


    def remove(self, node, value):

        if node.value == value:
            if node.leftChild == None and \
                node.rightChild == None:

                # get parent
                parent = None
                temp = self.root
                while True:
                    parent = temp
                    if node.value < temp.value:
                        temp = temp.leftChild
                    elif node.value > temp.value:
                        temp = temp.rightChild
                    else:
                        temp = node
                        break

                if parent.leftChild == node:
                    parent.leftChild = None
                else:
                    parent.rightChild = None

                return temp

            elif node.leftChild and node.rightChild == None:
                # Go as far right as possible
                right = self.find_max(node.leftChild)

                # Copy the right most node's value into the current node's value
                node.value = right.value

                # Recurse with right most node.
                return self.remove(right, right.value)
            else:
                # Go as far left as possible
                left = self.find_min(node.rightChild)

                # Copy the left most node's value into the current node's value
                node.value = left.value

                # Recurse with left most node.
                return self.remove(left, left.value)                

        elif value < node.value:
            return self.remove(node.leftChild, value)
        else:
            return self.remove(node.rightChild, value)


    def remove_node(self, value):
        # Tree is empty/has no nodes
        if self.root == None:
            logger.info(f"The tree is empty!") 

        # Tree is not empty
        else:
            found = self.find_node(value)
            if found:
                del_node = self.remove(self.root, value)
                logger.info(f"Deleted {del_node.value}")
                return True
            else:
                logger.info("Node not found!")
                return False
        
        return


    def find_min(self, node):
        while node.leftChild:
            node = node.leftChild        
        return node


    def find_max(self, node):
        while node.rightChild:
            node = node.rightChild
        return node


    def preorder_traversal(self):
        # root -> left -> right
        s = Stack()
        s.push(self.root)
        visited = []

        while not s.is_empty():
            node = s.pop().value
            visited.append(node.value)

            if node.rightChild:
                s.push(node.rightChild)

            if node.leftChild:
                s.push(node.leftChild)

        logger.info(f"Preorder: {visited}")
        return       


    def inorder_traversal(self):
        # left -> root -> right
        s = Stack()
        s.push(self.root)
        visited = []
        left = False

        while not s.is_empty():
            while (s.top().value.leftChild and not left):
                s.push(s.top().value.leftChild)
            
            if s.top().value.rightChild:
                node = s.pop().value
                visited.append(node.value)
                s.push(node.rightChild)
                left = False
            else:
                # leaf
                visited.append(s.pop().value.value)
                left = True
        
        logger.info(f"Inorder: {visited}")
        return


    def postorder_traversal(self):
        # left -> right -> root
        s = Stack()
        s.push(self.root)
        visited_node = None
        visited = []

        while not s.is_empty():
            # import pdb; pdb.set_trace()
            if not s.top().value.rightChild and not s.top().value.leftChild:
                visited_node = s.pop().value.value
                visited.append(visited_node)
            
            elif s.top().value.rightChild != None and \
                s.top().value.rightChild.value == visited_node:
                    visited_node = s.pop().value.value
                    visited.append(visited_node)
            
            elif s.top().value.leftChild and \
                s.top().value.leftChild.value == visited_node:
                    visited_node = s.pop().value.value
                    visited.append(visited_node)

            else:
                top = s.top().value
                if top.rightChild:
                    s.push(top.rightChild)
                
                if top.leftChild:
                    s.push(top.leftChild)

        logger.info(f"Postorder: {visited}")
        return


    def level_order_traversal(self):
        q = Queue()
        q.enqueue(self.root)
        visited = []

        while not q.is_empty():
            node = q.dequeue().value
            if node.leftChild:
                q.enqueue(node.leftChild)
            
            if node.rightChild:
                q.enqueue(node.rightChild)

            visited.append(node.value)

            del(node)

        logger.info(f"Level order: {visited}")
        return