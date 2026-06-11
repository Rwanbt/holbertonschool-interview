#!/usr/bin/python3
"""
Module pour valider l'encodage UTF-8
"""


def validUTF8(data):
    """
    Détermine si une liste d'entiers est un encodage UTF-8 valide.
    """
    n_bytes = 0

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) == 0b10:
                n_bytes -= 1
            else:
                return False

    return n_bytes == 0
