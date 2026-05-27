#!/usr/bin/env python3
"""module for calculate the minimum operation number"""


def minOperations(n):
    """Calculate the minimum operations"""
    n = int
    if n <= 1:
        return 0

    operations = 0
    diviseur = 2

    while n > 1:
        while n % diviseur == 0:  # modulo
            operations += diviseur  # operations = operations + diviseur
            n //= diviseur  # n = n // diviseur
        diviseur += 1

    return operations
