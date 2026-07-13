#!/usr/bin/python3
"""
Module for Prime Game challenge.
"""


def isWinner(x, nums):
    """
    Determine the winner of x rounds of the Prime Game.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    prime_counts = [0] * (max_n + 1)
    current_count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            current_count += 1
        prime_counts[i] = current_count

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
