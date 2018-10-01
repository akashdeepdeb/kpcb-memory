# Memory
Making a fun, terminal, memory card game (also called Concentration)

### Instructions
Running the game is fairly straightforward.
Perform the following steps in the current directory:
```
    $ chmod +x memory.sh
    $ ./memory.sh
```
You should get the following terminal output, waiting for a response:
```
    ===== WELCOME TO THE MEMORY GAME HUMANS AND ROBOTS =====
    How many players would like to play memory today?
    Enter 1 to play with the computer or >2 to play with friends! 
```
This game can be multiplayer or single player (play with computer - which works like a FIFO Cache to preserve memory just like another player would)

Follow the instructions, and players will have to choose a location to flip a card. The format of a location is simply `{a-i}{1-6}`, analogous to a chess-board algebraic notation. 

To see how the game functions, go to file `printgame.py` and change `line 14` from `if False:` to `if True:`

### Rules
The object of this game is to find as many pairs of cards with the same rank. There are only 2 pairs of cards with the same rank which covers all suits. 

Rules are the same as the standard game. If a player, successfully finds a match, they receive 10 points on top of their current score. If the match is unsuccessful, the next player gets to move. 

### Design choice description

The game's organization is fairly flat and modular design with the use of additional class objects and other embedded data structures like the use of a FIFO Cache (instead of an LRU Cache).

- The game is set in `main.py` which calls on `gameplay.py` which contains all the main functions for the multiplyer version of this game. 
- `gameplay.py` calls on print functions provided in `printgame.py` which prints the current_board set up. 
- A `Card` class has been used to define all 54 cards as card objects. The printing functions utilize this data structure to print the board in a user-friendly manner. 
- `computer.py` is essentially a FIFO Cache that stores card information that it reads while playing with the opposite user. The algorithm this model uses is as follows:
     ```
     cache size depends on user level [capacity = 3*level]
     select first card randomly from the set
     for second card, look through cache
     if match:
        print both
        delete second card entry from cache
     if no match:
        select second car randomly from the set
        if match:
            print both
        if no match:
            append both to the cache and pop if overflow occurs
     ```
- `utils.py` has been used for utility functions that other files have commonly called. It makes more sense to make a general function for utility tools so all other classes and objects can import one file for such methods. 


### Tooling

Python 3.6.5 has been used for this project. I chose it because I use it most frequently and easier to read code if codebase is large. Choices were: Scala, Python, C++ and Python was the clear winner .
Additional python libraries used for util operations: `os, time, sys, random, subprocess`

### Comments and Feedback

If you have any questions or feedback for me on this game, feel free to email me at `deb2 at illinois dot edu` :)