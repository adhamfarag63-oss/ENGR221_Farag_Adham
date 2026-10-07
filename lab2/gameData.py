"""
Name: Adham Farag
Date: September 20, 2026
Description: Manages the game data and board state for Antarctic Survival (ENGR 221 Lab 2).
Handles player movement, neighbor retrieval, food generation, and enemy mechanics.
"""

import random
from Lab3.preferences import Preferences
from lab2.cell import Cell

class GameData:
    def __init__(self):
        """Initializes the board state, score, steps, and entity positions."""
        self.num_rows = Preferences.NUM_ROWS
        self.num_cols = Preferences.NUM_COLS
        
        # Construct 2D grid of Cell objects
        self.board = [[Cell(r, c) for c in range(self.num_cols)] for r in range(self.num_rows)]
        
        self.player_cell = self.board[0][0]
        self.player_cell.cell_type = Preferences.CELL_TYPE_PLAYER
        
        self.food_cells = []
        self.enemies = []
        
        self.score = 0
        self.steps = 0
        self.game_over = False

    # ==========================================
    # 2.1 Helper Functions: Neighbor Retrieval
    # ==========================================

    def get_west_neighbor(self, cell):
        """Returns the Cell directly to the left of given cell, or None if out of bounds."""
        if cell.col > 0:
            return self.board[cell.row][cell.col - 1]
        return None

    def get_east_neighbor(self, cell):
        """Returns the Cell directly to the right of given cell, or None if out of bounds."""
        if cell.col < self.num_cols - 1:
            return self.board[cell.row][cell.col + 1]
        return None

    def get_north_neighbor(self, cell):
        """Returns the Cell directly above given cell, or None if out of bounds."""
        if cell.row > 0:
            return self.board[cell.row - 1][cell.col]
        return None

    def get_south_neighbor(self, cell):
        """Returns the Cell directly below given cell, or None if out of bounds."""
        if cell.row < self.num_rows - 1:
            return self.board[cell.row + 1][cell.col]
        return None

    # ==========================================
    # 2.2 Player Movement Methods
    # ==========================================

    def move_player_to_cell(self, target_cell):
        """Helper to update board state when player moves to a target cell."""
        if target_cell is None or self.game_over:
            return

        # If stepping on an enemy, game over
        if target_cell in self.enemies or target_cell.cell_type == Preferences.CELL_TYPE_ENEMY:
            self.game_over = True
            return

        # If stepping on food, eat it
        if target_cell in self.food_cells or target_cell.cell_type == Preferences.CELL_TYPE_FOOD:
            self.eat_food(target_cell)

        # Clear old player position
        self.player_cell.cell_type = Preferences.CELL_TYPE_EMPTY
        
        # Set new player position
        self.player_cell = target_cell
        self.player_cell.cell_type = Preferences.CELL_TYPE_PLAYER

        # Increment step count and handle periodic spawns
        self.steps += 1
        if self.steps % 10 == 0:
            self.add_food()
        if self.steps % 50 == 0:
            self.add_enemy()

    def move_player_left(self):
        """Moves the player left one cell if possible."""
        target = self.get_west_neighbor(self.player_cell)
        self.move_player_to_cell(target)

    def move_player_right(self):
        """Moves the player right one cell if possible."""
        target = self.get_east_neighbor(self.player_cell)
        self.move_player_to_cell(target)

    def move_player_up(self):
        """Moves the player up one cell if possible."""
        target = self.get_north_neighbor(self.player_cell)
        self.move_player_to_cell(target)

    def move_player_down(self):
        """Moves the player down one cell if possible."""
        target = self.get_south_neighbor(self.player_cell)
        self.move_player_to_cell(target)

    # ==========================================
    # 2.3 Food Related Methods
    # ==========================================

    def add_food(self):
        """Adds a food cell at a random empty location on the board."""
        empty_cells = [
            cell for row in self.board for cell in row
            if cell.cell_type == Preferences.CELL_TYPE_EMPTY
        ]
        if empty_cells:
            target_cell = random.choice(empty_cells)
            target_cell.cell_type = Preferences.CELL_TYPE_FOOD
            self.food_cells.append(target_cell)

    def eat_food(self, target_cell):
        """Updates score and removes food cell when player eats food."""
        if target_cell in self.food_cells:
            self.food_cells.remove(target_cell)
        target_cell.cell_type = Preferences.CELL_TYPE_EMPTY
        self.score += 1

    # ==========================================
    # 2.4 Enemy Movement Methods
    # ==========================================

    def add_enemy(self):
        """Adds an enemy to the bottom-right corner of the board."""
        br_cell = self.board[self.num_rows - 1][self.num_cols - 1]
        
        # Check collision with player
        if br_cell == self.player_cell:
            self.game_over = True
            return

        # If bottom right has food, clear food tracking
        if br_cell in self.food_cells:
            self.food_cells.remove(br_cell)

        br_cell.cell_type = Preferences.CELL_TYPE_ENEMY
        if br_cell not in self.enemies:
            self.enemies.append(br_cell)

    def move_enemy_to_cell(self, idx, target_cell):
        """Moves enemy at index idx to target_cell and checks collisions."""
        if target_cell is None or idx >= len(self.enemies):
            return

        current_cell = self.enemies[idx]

        # Check collision with player
        if target_cell == self.player_cell:
            self.game_over = True
            return

        # Clear current enemy cell
        current_cell.cell_type = Preferences.CELL_TYPE_EMPTY
        
        # Handle food overwrite
        if target_cell in self.food_cells:
            self.food_cells.remove(target_cell)

        # Move enemy
        target_cell.cell_type = Preferences.CELL_TYPE_ENEMY
        self.enemies[idx] = target_cell

    def move_enemy_left(self, idx):
        """Moves enemy at index idx to the west neighbor cell."""
        if idx < len(self.enemies):
            target = self.get_west_neighbor(self.enemies[idx])
            self.move_enemy_to_cell(idx, target)

    def move_enemy_right(self, idx):
        """Moves enemy at index idx to the east neighbor cell."""
        if idx < len(self.enemies):
            target = self.get_east_neighbor(self.enemies[idx])
            self.move_enemy_to_cell(idx, target)

    def move_enemy_up(self, idx):
        """Moves enemy at index idx to the north neighbor cell."""
        if idx < len(self.enemies):
            target = self.get_north_neighbor(self.enemies[idx])
            self.move_enemy_to_cell(idx, target)

    def move_enemy_down(self, idx):
        """Moves enemy at index idx to the south neighbor cell."""
        if idx < len(self.enemies):
            target = self.get_south_neighbor(self.enemies[idx])
            self.move_enemy_to_cell(idx, target)
