#!/usr/bin/python3
"""Prime game.
"""


def isWinner(x, nums):
    """This game determines the winner, given 'x' rounds.
    """
    if x < 1 or not nums:
        return None
    maria_is_winner, ben_is_winner = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        num_of_primes = len(list(filter(lambda x: x, primes[0: n])))
        ben_is_winner += num_of_primes % 2 == 0
        maria_is_winner += num_of_primes % 2 == 1
    if maria_is_winner == ben_is_winner:
        return None
    return 'Maria' if maria_is_winner > ben_is_winner else 'Ben'
