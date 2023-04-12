#!/usr/bin/python3

import sys

"""Initialize variables"""


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    """Read input from standard input"""


    for line in sys.stdin:
        components = line.split()
        ip_address = components[0]
        status_code = int(components[8])
        file_size = int(components[9])
        
        total_size += file_size
        status_codes[status_code] += 1
        line_count += 1
        
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
