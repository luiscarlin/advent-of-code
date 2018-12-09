import checksum_calc

def test_repeated_returns_1_when_string_contains_repeated_char_twice():
  id = 'aa'
  actual = checksum_calc.repeated(id, 2)
  assert actual == 1

def test_repeated_returns_0_when_string_does_not_contain_repeated_char():
  id = 'ab'
  actual = checksum_calc.repeated(id, 2)
  assert actual == 0

def test_repeated_returns_1_when_string_contains_repeated_char_three_times():
  id = 'bacaca'
  actual = checksum_calc.repeated(id, 3)
  assert actual == 1