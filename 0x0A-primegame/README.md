# 0x0A. Prime Game

Building a game using python logic and mathematics. Algorithmic thinking.

## Tasks

0. Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine whothe winner of each game is.

- Prototype: def isWinner(x, nums)
- where x is the number of rounds and nums is an array of n
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return None
- You can assume n and x will not be larger than 10000
- You cannot import any packages in this task

## Output
`isWinner = __import__('0-prime_game').isWinner`

`print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))`

