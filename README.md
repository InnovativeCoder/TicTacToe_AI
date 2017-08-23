# TicTacToe_AI
Implementation of reinforcement learning on tictoactoe game.
This game AI learns the states and actions and memorize them by increasing or decreasing the value function.

**Temporal Difference Learning is used for making it learn the moves and choose best move.**



*Temporal Difference learning* :- Temporal difference (TD) learning is a prediction-based machine learning method. It has primarily been used for the reinforcement learning problem, and is said to be **"a combination of Monte Carlo ideas and dynamic programming (DP) ideas."** TD resembles a Monte Carlo method because it learns by sampling the environment according to some policy, and is related to dynamic programming techniques as it approximates its current estimate based on previously learned estimates (a process known as bootstrapping).


Steps to compile the file :- 
1. Clone the repository 
2. Change the directory to TicTacToe_AI
3. then type python tictactie.py for compilation.

Play the game and make your model learn the moves(only for single compilation). The values are currently stored in an array as of now, but soon will make changes for storing them in a csv file or an excel spreadsheet. THe states gereated recursively have been stored into the states.csv file hence reducing the compile time. 
