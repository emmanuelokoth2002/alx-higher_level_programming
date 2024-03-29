#!/usr/bin/python3

import sys

"""initialize variables and data structures"""

total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    """read input line by line"""

    for line in sys.stdin:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[8])
        file_size = int(parts[9])
        
        total_file_size += file_size
        status_codes[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")
            print("---")
            
except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

