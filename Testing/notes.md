Assert Statement - 
It is a debugging tool which interrupts the flow of
the code when the assert statement fails and does nothing when it passes

```python
def test_func():
    assert func.add(1,2) == 3 
```

# Class Test
```python
class TestClass:
    def setup_method(self,method):
        return 

    def teardown_method(self,method):
        return

```
The setup and tear down methods run at the beginning and end respetively of each test.*The naming conversion should be the same for it to apply.*. The method refers to the test that is beign run. 
`pytest -s test.py`

# Fixtures
In classes we have setup and tear down. But normal function tests fixtures
```python

```