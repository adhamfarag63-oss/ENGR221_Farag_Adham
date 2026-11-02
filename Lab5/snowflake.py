"""
Name: Adham Farag
Date last updated: November 1, 2026
Description: Draws a Koch snowflake (a fractal curve built on an equilateral
             triangle) using Python's turtle module. Each of the three sides
             is drawn two ways: recursively (draw_curve_recursive_helper) and
             non-recursively with an explicit stack of commands
             (draw_curve_stack). compare_snowflake() reports the time and
             memory used by each approach.
"""

import turtle
import time 
from memory_profiler import memory_usage

class KochSnowflake:
    def __init__(self, init_length=500, init_depth=3):
        # Initialize the turtle
        self.t = None  

        # Length of one edge at 0 depth
        self.init_length = init_length  
        # Number of "layers" to draw
        self.init_depth = init_depth    
    

    def init_turtle(self):
        """ Initialize the turtle and move it to the 
            appropriate location on the screen """
        
        t = turtle.Turtle() # Initialize the turtle
        t.speed(8) # Increase the turtle's speed
        # Move the turtle to the upper left corner
        t.penup()
        t.goto(-200, -200)
        t.pendown()
        self.t = t


    ######################
    # Draw curve methods #
    ######################

    def draw_curve_recursive(self):
        """ The 'entry point' into the recursive curve method """
        self.draw_curve_recursive_helper(self.init_length, self.init_depth)


    def draw_curve_recursive_helper(self, length, depth):
        """ Recursively draw one side of the Koch snowflake.

            At depth 0 the side is just a straight line of the given length.
            At any other depth, the side is replaced by four curves of
            one-third the length and one less depth, joined by turns that form
            an outward-pointing "bump" (turn right 60, left 120, right 60).

            length: the length of this side (in turtle units)
            depth:  how many more times the side should be subdivided """

        # Raise an error if depth is negative
        if depth < 0:
            raise "Depth cannot be negative"

        # Base case
        elif depth == 0:
            self.t.forward(length)

        # Recursive case
        else:
            new_length = length / 3
            new_depth = depth - 1

            self.draw_curve_recursive_helper(new_length, new_depth)
            self.t.right(60)
            self.draw_curve_recursive_helper(new_length, new_depth)
            self.t.left(120)
            self.draw_curve_recursive_helper(new_length, new_depth)
            self.t.right(60)
            self.draw_curve_recursive_helper(new_length, new_depth)


    def draw_curve_stack(self):
        """ Draw one side of the Koch snowflake WITHOUT recursion, using a
            stack of commands to emulate the call stack.

            Commands are tuples:
              ("add_curve", length, depth) - draw a curve (straight line if
                                             depth == 0, otherwise expand it)
              ("turn_left", angle)         - turn left by angle degrees
              ("turn_right", angle)        - turn right by angle degrees
            A stack is last-in, first-out, so the commands for an expanded
            curve are pushed in REVERSE of the order they should run. """
        
        commands = [("add_curve", self.init_length, self.init_depth)]

        while commands:
            command = commands.pop()

            if command[0] == "add_curve":
                _, length, depth = command

                # Base case: draw a straight line
                if depth == 0:
                    self.t.forward(length)

                # Otherwise push the expanded curve (in reverse order)
                else:
                    new_length = length / 3
                    new_depth = depth - 1

                    commands.append(("add_curve", new_length, new_depth))
                    commands.append(("turn_right", 60))
                    commands.append(("add_curve", new_length, new_depth))
                    commands.append(("turn_left", 120))
                    commands.append(("add_curve", new_length, new_depth))
                    commands.append(("turn_right", 60))
                    commands.append(("add_curve", new_length, new_depth))

            elif command[0] == "turn_left":
                self.t.left(command[1])

            elif command[0] == "turn_right":
                self.t.right(command[1])


    ##########################
    # Draw snowflake methods #
    ##########################

    def draw_snowflake_recursive(self):
        """ Draw the three edges of the Koch snowflake using the 
            recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_recursive()
            self.t.left(120)
            
        turtle.clearscreen()


    def draw_snowflake_stack(self):
        """ Draw the three edges of the Koch snowflake using the 
            non-recursive curve method """

        self.init_turtle()

        for _ in range(3):
            self.draw_curve_stack()
            self.t.left(120)

        turtle.clearscreen()


    #########################@#
    # Compare the approaches! #
    ##########################@

    def compare_snowflake(self):
        """ Compare how much time and memory the recursive and non-recursive 
            implementations of drawing the Koch Snowflake used """
        
        rec_time, rec_mem = self.get_time_and_mem(self.draw_snowflake_recursive)
        nonrec_time, nonrec_mem = self.get_time_and_mem(self.draw_snowflake_stack)

        print(f"Recursive memory usage: {rec_mem} MB")
        print(f"Non-recursive memory usage: {nonrec_mem} MB")
        print()
        print(f"Recursive time taken: {rec_time:.5f} s")
        print(f"Non-recursive time taken: {nonrec_time:.5f} s")
        

    def get_time_and_mem(self, func):
        """ Find the time and memory used by the given function """

        # Start the timer
        time_start = time.perf_counter()
        # Run the function and find the memory used
        mem_usage = memory_usage((func, ), include_children=True, multiprocess=True)
        # End the timer
        time_end = time.perf_counter()

        # Find the total time taken
        time_taken = time_end - time_start 
        # Find the total memory used
        mem_used = max(mem_usage) - min(mem_usage)

        return time_taken, mem_used


if __name__ == "__main__":
    s = KochSnowflake(500, 3)
    s.draw_snowflake_stack()

