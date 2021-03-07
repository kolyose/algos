def create_test_runner(fn):
  print(f'Testing function {fn.__module__}.{fn.__name__}:')

  def test(cases):
    counter = 1;
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
