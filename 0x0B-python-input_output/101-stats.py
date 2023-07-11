#!/usr/bin/python3
""" Dictionary to store status code counts"""
import sys
import signal

status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

# Variable to keep track of total file size
total_file_size = 0

# Variable to count the number of lines read
line_count = 0


def print_statistics(signal, frame):
    """
    Print the statistics when the signal (keyboard interruption) is received.

    Args:
        signal: The signal number.
        frame: The current stack frame.

    Returns:
        None

    """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        if count > 0:
            print(status_code + ":", count)
    sys.exit(0)

# Register the signal handler


signal.signal(signal.SIGINT, print_statistics)

try:
    for line in sys.stdin:
        line = line.strip()
        if line:
            # Split the line by space
            parts = line.split(" ")
            if len(parts) >= 9:
                status_code = parts[7]
                file_size = parts[8]

                # Update the status code count
                if status_code in status_counts:
                    status_counts[status_code] += 1

                # Update the total file size
                try:
                    total_file_size += int(file_size)
                except ValueError:
                    pass

                line_count += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print("Total file size:", total_file_size)
                    for status_code in sorted(status_counts):
                        count = status_counts[status_code]
                        if count > 0:
                            print(status_code + ":", count)
                    print()
except KeyboardInterrupt:
    pass

# Print the final statistics
print_statistics(None, None)
