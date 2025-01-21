# Simple-ChessAI

Project for my Introduction to Artificial Intelligence which start out focusing on different fundamentals such as agents, the types of environment they operate in and important agent algorithms such as aplha-beta pruning.

## How it works

The minimax function is a recursive algorithm used to find the optimal move in a game by evaluating the board's state. It terminates when the depth is 0 or the game is over, returning an evaluation of the board. 

For each player, it tries all legal moves, pushes each move onto the board, calls minimax recursively for the other player, and updates the best move and evaluation found, while pruning branches where alpha is greater than or equal to beta. Alpha-beta pruning allows minimax to optimize the search process by ignoring branches that will not affect the final decision.

## Dependencies
This assignment is written completely in python and makes use of the python chess library to manipulate and observe the gameplay.

To install python chess library run:
    
    pip install python-chess

To start the game open terminal and enter: 
    
    python3 chess_agent.py
