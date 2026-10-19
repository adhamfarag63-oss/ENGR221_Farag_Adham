"""
Author: YOUR NAME HERE
Last updated: October 16, 2026
Description: Custom Stack and Queue classes used by the Duck Collector AI.
Both classes expose the same three methods (add, remove, is_empty) so that
the same search code can run as depth-first search (with a Stack) or
breadth-first search (with a Queue) just by swapping the structure.
"""

class Queue():
    """ A first-in, first-out (FIFO) structure. Items are added to the
        end of the list and removed from the beginning of the list. """

    def __init__(self):
        # The items in the queue; index 0 is the front of the queue
        self.items = []

    def add(self, item) -> None:
        """ "Enqueue" the item to the end of the queue """
        self.items.append(item)

    def remove(self):
        """ "Dequeue" the item from the front of the queue and return it """
        return self.items.pop(0)

    def is_empty(self) -> bool:
        """ Returns whether or not the queue is empty """
        return len(self.items) == 0


class Stack():
    """ A first-in, last-out (FILO) structure. Items are added to the end
        of the list and removed from the end of the list. """

    def __init__(self):
        # The items in the stack; the last index is the top of the stack
        self.items = []

    def add(self, item) -> None:
        """ Push an item to the top (end) of the stack """
        self.items.append(item)

    def remove(self):
        """ Pop the item from the top (end) of the stack and return it """
        return self.items.pop()

    def is_empty(self) -> bool:
        """ Returns whether or not the stack is empty """
        return len(self.items) == 0
