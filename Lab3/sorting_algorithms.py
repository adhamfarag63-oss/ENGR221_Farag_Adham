"""
Author: Adham Farag
Last updated: October 7, 2026
Description: Stores the array to be sorted and implements the sorting
algorithms (selection sort, insertion sort, and bubble sort) used by the
Sorting Algorithm Visualizer. Each algorithm is a generator that yields a pair
of indices (outer, inner) at each step so the GUI can highlight those carrots.
Also includes get_runtime() for timing how long an algorithm takes.
"""

import random
import time

from Lab3.preferences import Preferences

class SortingAlgorithms:
    def __init__(self):
        # The algorithm to sort
        self.array = []

        # Any indices to highlight
        self.inner_idx = -1
        self.outer_idx = -1 

        # A string representing the current sorting algorithm
        self.current_alg = None

        # Store the method of the sorting algorithm being run
        self.alg_method = None
    
    def create_new_array(self, length=Preferences.NUM_ELEMENTS) -> list:
        """ Create a new array to sort """
        return [random.randint(0, Preferences.MAX_VAL) \
                      for _ in range(length)]
    
    def get_next_step(self) -> None:
        """ Updates the value of self.selected_idx whenever we reach 
            a "yield" statement in any of the below sorting algorithms. """
        
        try:
            # Treats the current sorting algorithm as an iterator
            # and sets self.selected_idx to be the next "element"
            self.outer_idx, self.inner_idx = next(self.alg_method)
        # Clear the selected_idx value when we reach the end of the method
        except StopIteration:
            self.outer_idx, self.inner_idx = -1, -1

    def restart(self, new_alg, length=Preferences.NUM_ELEMENTS) -> None:
        """ Restart the sorting process with the new algorithm. 
            Creates a new array to sort. """
        
        self.current_alg = new_alg
        self.alg_method = {
            "selection" : self.selection_sort,
            "insertion" : self.insertion_sort,
            "bubble" : self.bubble_sort
        }[self.current_alg]()
        self.array = self.create_new_array(length)
        self.outer_idx, self.inner_idx = -1, -1

    def selection_sort(self):
        """ An implementation of the Selection sorth algorithm. 
            A generator function which creates an iterator that 
            iterates through each "yielded" value. """
        
        # Number of items in the list
        n = len(self.array)

        # i is the first position of the unsorted part; everything before i is already sorted
        for i in range(n):
            # Show the position we are about to fill (red bar at index i)
            yield -1, i
            # Assume the item at position i is the smallest so far
            min_idx = i

            # Scan the rest of the unsorted part looking for something smaller
            for j in range(i + 1, n):
                # Show the current minimum (blue) and the item being compared to it (red)
                yield min_idx, j

                # If this item is smaller than the current minimum...
                if self.array[j] < self.array[min_idx]:
                    # ...remember its index as the new minimum
                    min_idx = j 
            
            # Swap the smallest item found into position i
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            # Show the two items that were just swapped
            yield i, min_idx
                

    def insertion_sort(self):
        """ An implementation of the Insertion sort algorithm. 
            Sorts self.array in place. A generator function which 
            yields the indices to highlight at each step. """

        # Number of items in the list
        n = len(self.array)

        # Everything before index i is sorted; insert item i into that part
        for i in range(n):
            # j tracks where the item being inserted currently sits
            j = i
            # Show the item we are about to insert
            yield -1, j

            # Swap the item left while its left neighbor is bigger
            while j > 0 and self.array[j - 1] > self.array[j]:
                self.array[j - 1], self.array[j] = self.array[j], self.array[j - 1]
                j -= 1
                # Show the item that moved (red) and the item it passed (blue)
                yield j + 1, j


    def bubble_sort(self):
        """ An implementation of the Bubble sort algorithm. 
            Sorts self.array in place. A generator function which 
            yields the indices to highlight at each step. """

        # Number of items in the list
        n = len(self.array)

        # Each pass bubbles the largest remaining item to the end
        for i in range(n):
            # Track whether this pass made any swaps
            swapped = False
            # Only compare items that are not yet in their final place
            for j in range(0, n - i - 1):
                # Swap neighbors that are out of order
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
                # Show the pair of neighbors that was just compared
                yield j, j + 1
            # If no swaps happened, the list is already sorted
            if not swapped:
                break

    def get_runtime(self) -> float:
        """ Returns the length of time (in seconds) that it took for 
            the function_to_run to sort a list of length list_length """

        # Get the time before running
        start_time = time.time()
        # Sort the given list
        for _ in self.alg_method:
            pass
        # Get the time after running
        end_time = time.time()
        # Return the difference
        return end_time - start_time

if __name__ == "__main__":
    s = SortingAlgorithms()
    s.restart("selection", 100)
    print(s.get_runtime())