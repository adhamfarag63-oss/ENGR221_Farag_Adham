# Lab 4: Duck Collector (BFS and DFS)

A Snake-style game where a horse (the player) collects ducks (food). Each
collected duck joins the line behind the horse. Stepping off the map or onto a
collected duck ends the game. Press `a` to let the AI play, using breadth-first
search (default) or depth-first search to find the nearest duck.

## Files

| File | What it does | Modified? |
|------|--------------|-----------|
| `game_data.py` | Game state (board, body, food, score), player movement, and the AI search. | **Yes** |
| `search_structure.py` | Custom `Stack` (FILO) and `Queue` (FIFO) classes with `add()`, `remove()`, `is_empty()`. | **Yes** |
| `cell.py` | Represents one cell on the board (type, search parent, search flags). | No |
| `controller.py` | Main game loop, key handling, and per-cycle updates. Run this file to play. | No |
| `display.py` | Draws the board and score with pygame. | No |
| `preferences.py` | Constants (board size, colors, timing, images). | No |
| `images/` | Horse and duck pictures. | No |
| `tests/structures_tests.py` | pytest tests for `Stack` and `Queue`. | No |
| `answers.txt` | Written answers to the homework questions. | New |
| `pseudocode.txt` | Pseudocode for `move_player_to_cell()` and `get_first_cell_in_path()`. | New |

### Changes in `game_data.py`
- `move_player_to_cell()`: collect ducks (grow) or move forward (tail follows).
- `get_next_cell_ai()`: BFS or DFS search for the closest duck.
- `get_first_cell_in_path()`: walks the search parents back to the first step.

## How to run

Install the dependencies:

    pip install pygame pytest

Play the game (arrow keys or i/j/k/l to steer, `a` for AI mode, any key to start):

    python3 controller.py

To run the AI with DFS instead of BFS, change the last line of `controller.py` to:

    Controller("dfs").run()

Run the tests from this folder:

    pytest -v -m stack tests/structures_tests.py
    pytest -v -m queue tests/structures_tests.py

(On Windows, use `py -m pytest ...` and `.\tests\structures_tests.py`.)
