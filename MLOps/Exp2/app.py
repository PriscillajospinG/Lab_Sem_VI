"""Simple utility functions for CI testing.

This module is intentionally small and beginner-friendly so that
students can focus on understanding the CI pipeline.
"""


def add_numbers(a: float, b: float) -> float:
	"""Return the sum of two numbers."""
	return a + b


def is_even(number: int) -> bool:
	"""Return True if the input integer is even, else False."""
	return number % 2 == 0


if __name__ == "__main__":
	print("Sample run for CI exercise")
	print(f"10 + 5 = {add_numbers(10, 5)}")
	print(f"Is 10 even? {is_even(10)}")
