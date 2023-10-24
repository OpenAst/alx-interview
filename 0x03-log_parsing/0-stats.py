#!/usr/bin/python3

import sys

TOTAL_FILE_SIZE = 0
STATUS_CODE_COUNTS = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
LINE_COUNT = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, _, _, _, _, status_code, file_size = parts

        try:
            status_code = int(status_code)
            if status_code in STATUS_CODE_COUNTS:
                STATUS_CODE_COUNTS[status_code] += 1
                TOTAL_FILE_SIZE += int(file_size)
                LINE_COUNT += 1
        except ValueError:
            pass

        if LINE_COUNT >= 10:
            print(f"Total file size: File size: {TOTAL_FILE_SIZE}")
            for code, count in sorted(STATUS_CODE_COUNTS.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print("----")
            LINE_COUNT = 0

except KeyboardInterrupt:
    print("Total file size: File size:", TOTAL_FILE_SIZE)
    for code, count in sorted(STATUS_CODE_COUNTS.items()):
        if count > 0:
            print(f"{code}: {count}")

print("Total file size: File size:", TOTAL_FILE_SIZE)
for code, count in sorted(STATUS_CODE_COUNTS.items()):
    if count > 0:
        print(f"{code}: {count}")
