# minesweeper

Minesweeper AI
This repository contains a Python implementation of the classic Minesweeper game along with an AI that uses logical inference to play the game. The AI makes moves based on known information about safe cells and mines.

Classes

Minesweeper
This class represents the Minesweeper game.

Methods

__init__(self, height=8, width=8, mines=8): Initializes the game board with the given height, width, and number of mines.
print(self): Prints a text-based representation of where mines are located.
is_mine(self, cell): Returns True if the cell contains a mine, False otherwise.
nearby_mines(self, cell): Returns the number of mines within one row and column of the given cell.
won(self): Checks if all mines have been flagged.
Sentence
This class represents a logical statement about the Minesweeper game. A sentence consists of a set of board cells and a count of the number of those cells which are mines.

Methods

__init__(self, cells, count): Initializes a sentence with the given cells and count.
__eq__(self, other): Checks if two sentences are equal.
__str__(self): Returns a string representation of the sentence.
known_mines(self): Returns the set of all cells in the sentence known to be mines.
known_safes(self): Returns the set of all cells in the sentence known to be safe.
mark_mine(self, cell): Updates the sentence given the fact that a cell is known to be a mine.
mark_safe(self, cell): Updates the sentence given the fact that a cell is known to be safe.
MinesweeperAI
This class represents the AI player for Minesweeper.

Methods

__init__(self, height=8, width=8): Initializes the AI with the given height and width.
mark_mine(self, cell): Marks a cell as a mine and updates all knowledge.
mark_safe(self, cell): Marks a cell as safe and updates all knowledge.
get_neighbors(self, cell): Returns a set of all cells neighboring the given cell.
add_knowledge(self, cell, count): Called when the Minesweeper board tells us, for a given safe cell, how many neighboring cells have mines in them.
make_safe_move(self): Returns a safe cell to choose on the Minesweeper board.
make_random_move(self): Returns a move to make on the Minesweeper board.
Usage

Initialize the Game: Create an instance of the Minesweeper class.
Initialize the AI: Create an instance of the MinesweeperAI class.
Make Moves: Use the AI to make moves by calling make_safe_move or make_random_move.
Update Knowledge: After making a move, update the AI's knowledge base using the add_knowledge method.
