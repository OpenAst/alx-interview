def isWinner(x, nums):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to simulate the game for a particular round
    def play_game(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        primes_set = set(primes)
        turn = 1  # Maria's turn is denoted by 1, Ben's turn is denoted by 2
        while primes_set:
            playable = [num for num in primes_set if num <= n]
            if not playable:
                break
            if turn == 1:  # Maria's turn
                for num in playable:
                    primes_set -= set(range(num, n + 1, num))
                turn = 2
            else:  # Ben's turn
                for num in playable:
                    primes_set -= set(range(num, n + 1, num))
                turn = 1
        return turn == 1  # If it's Maria's turn, Ben wins; otherwise, Maria wins

    # Count the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the winner with the most rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

