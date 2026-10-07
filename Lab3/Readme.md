Lab 3: Sorting Algorithms

Name: Adham Farag
ENGR 221

Overview

A program that sorts carrots by length so they can be bagged. It visualizes each step
of three sorting algorithms (selection sort, insertion sort, and bubble sort) in a
pygame window. Highlighted carrots show which items the algorithm is currently
looking at: blue is the outer index and red is the inner index.

Files

| File | What it does | Modified? |
|------|--------------|-----------|
| `controller.py` | Runs the main loop and handles key presses, then updates and draws each step. | No |
| `display.py` | Draws the carrots (or bars) and the instruction text in the window. | No |
| `preferences.py` | Stores constants such as sizes, colors, timing, and image paths. | No |
| `sorting_algorithms.py` | Stores the array and implements selection sort, insertion sort, and bubble sort as generators, plus `get_runtime()` for timing. | **Yes**: commented `selection_sort()`, implemented `insertion_sort()` and `bubble_sort()`, added the header and docstrings. |
| `answers.txt` | Written answers for Parts 1 through 5, including the bubble sort trace table and the runtime results. | **New** |
| `README.md` | This file. | **New** |
| `images/` | `carrot.png`, `carrot_inner.png`, and `carrot_outer.png`, used by the display. | No |

How to run

1. Install the dependency: `pip3 install pygame`
2. Open a terminal in this folder: `cd Lab3`
3. Start the visualizer: `python3 controller.py`

Controls

| Key | Action |
|-----|--------|
| `S` | Start selection sort on a new random array |
| `I` | Start insertion sort on a new random array |
| `B` | Start bubble sort on a new random array |
| `R` | Reset with a new array using the current algorithm |
| Right arrow or `L` | Advance one step |
| Space | Start or stop advancing continuously |

Timing the algorithms

`sorting_algorithms.py` can be run on its own to time an algorithm:

1. In the `if __name__ == "__main__":` block at the bottom, change
   `s.restart("selection", 100)` to `"insertion"` or `"bubble"`, and change the
   list size to `1000` or `10000`.
2. Run `python3 sorting_algorithms.py`. It prints the time in seconds.

The results are recorded in `answers.txt`.