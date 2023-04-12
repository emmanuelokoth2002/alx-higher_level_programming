#!/usr/bin/python3

import sys
from collections import defaultdict

"""Initialize variables to hold metrics"""


total_size = 0
status_counts = defaultdict(int)

try:
    """Read stdin line by line"""


    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_size += file_size
        status_counts[status_code] += 1

        if i % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")
            print()

except KeyboardInterrupt:
    print(f"\nTotal file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
