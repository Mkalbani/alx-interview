import sys
import collections

"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
 Define a dictionary to store the number of lines by status code.
status_code_counts = collections.defaultdict(int)

# Define a variable to store the total file size.
total_file_size = 0

# Read stdin line by line.
for line in sys.stdin:

    # Split the line into tokens.
    tokens = line.split()

    # Check if the line is in the expected format.
    if len(tokens) != 7 or not tokens[4].isdigit() or not tokens[6].isdigit():
        continue

    # Get the status code and file size.
    status_code = int(tokens[4])
    file_size = int(tokens[6])

    # Increment the number of lines for the given status code.
    status_code_counts[status_code] += 1

    # Update the total file size.
    total_file_size += file_size

    # Print the statistics every 10 lines and/or on keyboard interruption.
    if len(status_code_counts) % 10 == 0 or sys.stdin.isatty():
        print("File size:", total_file_size)

        # Print the number of lines by status code in ascending order.
        for status_code in sorted(status_code_counts):
            print(f"{status_code}: {status_code_counts[status_code]}")

# Print the statistics one last time if the script is not interrupted.
if not sys.stdin.isatty():
    print("File size:", total_file_size)

    # Print the number of lines by status code in ascending order.
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")
