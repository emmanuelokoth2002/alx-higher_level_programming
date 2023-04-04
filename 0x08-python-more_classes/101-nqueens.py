#!/usr/bin/python3
import sys

"""Check that the correct number of arguments were passed"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

"""Try to parse N as an integer"""

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

"""Check that N is at least 4"""

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

"""Define a function to check if a proposed solution is valid"""

def is_valid(solution):
    for i in range(N):
        for j in range(i + 1, N):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i:
                return False
    return True

"""Define a recursive function to find all solutions"""

def find_solutions(solution):
    if len(solution) == N:
        if is_valid(solution):
            print(' '.join(str(x) for x in solution))
    else:
        for i in range(N):
            if i not in solution:
                find_solutions(solution + [i])

"""Call the recursive function with empty solution"""

find_solutions([])
