# Pascal's Triangle Generator

This Python script generates Pascal's triangle of a specified height `n` and returns it as a list of lists of integers. Pascal's triangle is a triangular array of binomial coefficients, where each number is the sum of the two numbers directly above it.

## Usage

To use the Pascal's Triangle Generator, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone this repository or download the `pascal_triangle.py` file.

3. Import the `pascal_triangle` function into your Python script or interactive environment.

4. Call the `pascal_triangle` function with the desired height `n` as an argument to generate Pascal's triangle.

```python
from pascal_triangle import pascal_triangle

# Generate Pascal's triangle of height 5
result = pascal_triangle(5)
print(result)
