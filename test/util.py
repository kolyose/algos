"""Test utilities."""

def create_test_runner(fn):
  """Create test runner for `fn`.

  A Decorator wrapping a function under the test with another function that:
    - accepts a list of test cases along with expected values
    - prints `__module__` and `__name__` of the function under the test
    - calls the function under the test for each individual test case and asserts the result against the expected one
    - prints whether the test passed

  Arguments:
    - fn - a function under the test

  Returns: the wrapper function.
  """
  print(f'Testing function {fn.__module__}.{fn.__name__}:')

  def test(cases):
    counter = 1;
    actual = None
    
    for args, expected in cases:
      try:
        actual = fn(*args)
        assert actual == expected
      except:
        print(f'  ❌ {counter}: {actual} != {expected}')
      else:
        print(f'  ✅ {counter}: {actual} == {expected}')
      finally:
        counter += 1
        
  return test
