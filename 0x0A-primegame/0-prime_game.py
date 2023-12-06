#!/usr/bin/python3
"""Prime Game
"""

def is_prime(num):
    """Check for number primality.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of the prime game
    """
    def winner(n):
        """Even or odd, Maria or Ben
        """
        return "Maria" if n % 2 == 0 else "Ben"

    winners = []
    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        remaining = n # Keep the state of the num
        player = 1 # 1 for Maria, 2 for Ben

        while remaining > 0:
            found = False
            for p in primes:
                if remaining >= p:
                    found = True
                    remaining -= (remaining // p) * p
                    break


            if not found:
                break

            player = 3 - player # Swithc player

        winners.append(winner(3 - player)) # switch back to the last player

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
