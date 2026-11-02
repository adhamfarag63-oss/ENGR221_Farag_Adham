# Lab 5: Recursion (Koch Snowflake)

## Files
- `snowflake.py` - Draws a Koch snowflake with Python's `turtle` module. The
  `KochSnowflake` class draws each of the three sides in two ways:
  - **Recursively** (`draw_curve_recursive_helper`)
  - **Non-recursively** with an explicit stack of commands (`draw_curve_stack`)

  `compare_snowflake()` runs both approaches and prints the time and memory
  each one used.
- `answers.txt` - Answers to the questions in Parts 1 and 4.
- `pseudocode.txt` - Pseudocode for both curve methods (submitted on Canvas).

## How to run
1. Install the memory profiler: `pip install memory_profiler`
2. From the `Lab5` folder, run: `python snowflake.py`
3. A turtle window opens and draws the snowflake with the stack method. Change
   the second argument of `KochSnowflake(500, 3)` at the bottom of
   `snowflake.py` to change the depth.
4. To compare the two approaches, replace the last line of the
   `if __name__ == "__main__":` block with `s.compare_snowflake()`.
