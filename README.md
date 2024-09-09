# 2048 Game

This project is a Python implementation of the popular game *2048*, developed using the Pygame library. The goal of the game is to combine tiles with the same numbers by moving them up, down, left, or right to reach the 2048 tile.

## Features

- *Gameplay*: Play the classic 2048 game with smooth tile merging animations and intuitive controls.
- *Undo Feature*: Allows the player to undo the last move to correct mistakes.
- *High Score Tracking*: Keeps track of the highest score achieved by the player and saves it across game sessions.
- *Restart Option*: Restart the game at any time with a dedicated button.
- *Game Over and Win Screens*: Displays game over and win messages when appropriate conditions are met.

## Prerequisites

Before running the game, ensure that you have Python installed along with the required libraries:

1. [Python](https://www.python.org/downloads/) (version 3.7 or higher recommended)
2. [Pygame](https://www.pygame.org/news)

You can install Pygame using pip:

bash
pip install pygame


## How to Play

1. *Objective*: Combine tiles with the same number to form a tile with the number 2048.
2. *Controls*:
   - *Arrow Keys*: Move the tiles up, down, left, or right.
   - *R Key*: Restart the game.
   - *X Key*: Undo the last move.
3. *Scoring*: Earn points by merging tiles. The goal is to maximize your score while reaching the 2048 tile.
4. *Winning*: When you create a tile with the number 2048, you win! You can choose to continue playing or start a new game.
5. *Losing*: The game ends when there are no possible moves left on the board.

## Running the Game

1. Ensure all scripts (2048.py) are in the same directory.
2. Run the 2048.py script to start the game:

   bash
   python 2048.py
   

## Game Components

### Key Classes and Functions

1. **TwentyFortyEight Class**: Handles all the game logic, including tile movements, merging, and scoring.
   - **init()**: Initializes the game board and sets the initial state.
   - **moveUp(), moveDown(), moveLeft(), moveRight()**: Handles the tile movement and merging logic for each direction.
   - **random()**: Generates new tiles (2 or 4) at random positions after each move.
   - **highScore()**: Tracks the highest score achieved and saves it to a file.
   - **undo()**: Allows the player to revert the last move.
   - **game_over()**: Displays the game over screen when no more moves are possible.
   - **win()**: Displays the win screen when a 2048 tile is reached.
   - **run()**: The main game loop that handles player input, updates the game state, and renders the graphics.

2. *Drawing Functions*:
   - **draw_background()**: Draws the game board and grid lines.
   - **draw_numbers()**: Displays the numbers on the tiles based on their values.
   - **button()**: Creates the Restart and Undo buttons.

### Game Logic

- The game initializes with a 4x4 grid and randomly places two tiles (2 or 4) on the board.
- On each move, tiles slide in the chosen direction, merging if they have the same value.
- A new tile (2 or 4) is added to a random empty spot after each move.
- The game checks for win (reaching 2048) and lose (no available moves) conditions.

## Saving High Scores

- High scores are saved in a text file (highscore.txt) within the same directory as the game script. If the file does not exist, it is created automatically.

## Future Improvements

- Add sound effects and music for a more immersive experience.
- Implement more advanced animations for tile merging and movement.
- Add levels or varying grid sizes for increased difficulty.
