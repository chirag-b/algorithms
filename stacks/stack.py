# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of a stack 
# using a doubly linked list
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#    - LIFO -> last in first out
#    - Push nodes onto stack
#    - Remove top node from stack
#    - Size, peek, get last element
# -----------------------------------------------

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

logger.info(sys.path)