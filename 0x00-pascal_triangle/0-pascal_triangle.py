#!/usr/bin/python3  # Shebang line indicating the Python interpreter to use

def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    triangle = [[1]]  # Initialize a list with the first row [1]

    for _ in range(1, n):  # Loop from the second row (row index 1) to the nth row
        prev_row = triangle[-1]  # Get the last row of the current triangle
        new_row = [1]  # Create a new row with the first element as 1

        for i in range(1, len(prev_row)):  # Loop through the previous row
            # Calculate the middle elements by adding two adjacent elements from the previous row
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)  # Add the last element of the new row, which is always 1
        triangle.append(new_row)  # Append the new row to the triangle

    return triangle  # Return the generated Pascal's triangle
