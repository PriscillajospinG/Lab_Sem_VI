from app import add_numbers, is_even


def test_add_numbers_positive_values() -> None:
	assert add_numbers(2, 3) == 5


def test_add_numbers_negative_values() -> None:
	assert add_numbers(-2, -8) == -10


def test_add_numbers_float_values() -> None:
	assert add_numbers(2.5, 1.5) == 4.0


def test_is_even_with_even_number() -> None:
	assert is_even(10) is True


def test_is_even_with_odd_number() -> None:
	assert is_even(7) is False
