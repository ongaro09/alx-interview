#!/usr/bin/python3
import sys
import signal
from typing import Dict, Any

# Initialize metrics
total_size: int = 0
status_counts: Dict[str, int] = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count: int = 0


def print_stats() -> None:
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig: int, frame: Any) -> None:
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            # Extract status code and file size
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            global total_size
            total_size += file_size

            # Update status code count if valid
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            continue

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
