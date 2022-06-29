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


    def insert_node(self, value, root=None):
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
                    self.insert_node(value, root.leftChild)
                else:
                    root.leftChild = Node(None, None, value)
                    logger.info(f"Node {value} inserted!")
            else:
                if root.rightChild != None:
                    self.insert_node(value, root.rightChild)
                else:
                    root.rightChild = Node(None, None, value)
                    logger.info(f"Node {value} inserted!")
        
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
                logger.info(f"Found {value}!!!")
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
                print(f"Deleting {node.value}")
                return node

            elif node.leftChild and node.rightChild == None:
                # Go as far right as possible
                right = self.find_max(node.leftChild)

                # Copy the right most node's value into the current node's value
                node.value = right.value

                # Recurse with right most node.
                self.remove(right, right.value)
            else:
                # Go as far left as possible
                left = self.find_min(node.rightChild)

                # Copy the left most node's value into the current node's value
                node.value = left.value

                # Recurse with left most node.
                self.remove(left, left.value)                

        elif value < node.value:
            self.remove(node.leftChild, value)
        else:
            self.remove(node.rightChild, value)

        # # Case 1: Leaf node
        # if node.leftChild == None and \
        #     node.rightChild == None:
        #     print(f"Deleting {node.value}")
        #     del node
        #     return

        # # Case 2: Non-leaf node
        # else:
        #     if node.leftChild and node.rightChild == None:
        #         # Go as far right as possible
        #         right = self.dig_right(node.leftChild)

        #         # Copy the right most node's value into the current node's value
        #         node.value = right.value

        #         # Recurse with right most node.
        #         self.remove(right)
        #     else:
        #         # Go as far left as possible
        #         left = self.dig_left(node.rightChild)

        #         # Copy the left most node's value into the current node's value
        #         node.value = left.value

        #         # Recurse with left most node.
        #         self.remove(left)


    def remove_node(self, value):
        # Tree is empty/has no nodes
        if self.root == None:
            logger.info(f"The tree is empty!") 

        # Tree is not empty
        else:
            found = self.find_node(value)
            if found:
                node = self.remove(self.root, value)
                logger.info(f"Ref count {node.value}: {sys.gettotalrefcount(node)}")
                return True
            else:
                logger.info("Node not found!")
                return False
        
        return

    def find_max(self, node):
        while node.leftChild:
            node = node.leftChild        
        return node


    def find_min(self, node):
        while node.rightChild:
            node = node.rightChild
        return node


    def preorder_traversal(self):
        # root -> left -> right
        stack = Stack()
        stack.push(self.root)
        visited = []

        while not stack.is_empty():
            node = stack.pop()
            visited.append(node.value)

            if node.rightChild:
                stack.push(node.rightChild)

            if node.leftChild:
                stack.push(node.leftChild)

        logger.info(f"Preorder: {visited}")
        return       


    def inorder_traversal(self):
        # left -> root -> right
        s = Stack()
        s.push(self.root)
        visited = []
        left = False

        while not s.is_empty():
            while (s.top().leftChild and not left):
                s.push(s.top().leftChild)
            
            if s.top().rightChild:
                node = s.pop()
                visited.append(node.value)
                s.push(node.rightChild)
                left = False
            else:
                # leaf
                visited.append(s.pop().value)
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

            if not s.top().rightChild or s.top.rightChild == visited_node:
                visited_node = s.pop()
                visited.append(visited_node.value)
            
            else:
                if s.top().rightChild:
                    s.push(s.top().rightChild)

                if s.top().leftChild:
                    s.push(s.top().leftChild)

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