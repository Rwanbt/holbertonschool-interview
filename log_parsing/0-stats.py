#!/usr/bin/python3
"""
Script qui lit stdin ligne par ligne et calcule des métriques.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Affiche les statistiques accumulées.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_logs():
    """
    Lit sys.stdin et traite les logs.
    """
    total_size = 0
    line_count = 0

    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            parsed_line = line.split()

            if len(parsed_line) < 2:
                continue

            try:
                file_size = int(parsed_line[-1])
                status_code = parsed_line[-2]

                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1

            except (IndexError, ValueError):
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    parse_logs()
