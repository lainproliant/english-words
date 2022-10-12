#!/usr/bin/env python3
# --------------------------------------------------------------------
# comma.py
#
# Author: Lain Musgrove (lain.proliant@gmail.com)
# Date: Wednesday October 12, 2022
# --------------------------------------------------------------------

import sys


# --------------------------------------------------------------------
def main():
    line = sys.stdin.readline()

    while line:
        sys.stdout.write(line.strip())

        new_line = sys.stdin.readline()

        if new_line:
            sys.stdout.write(",")

        line = new_line

    for line in sys.stdin.readlines():
        sys.stdout.write(line.strip())
        sys.stdout.write(",")

# --------------------------------------------------------------------
if __name__ == '__main__':
    main()
