import math_file
import pytest

@pytest.mark.parametrize('num1, num2, res', [
    (5, 5, 10),
    ("Hello", "world", "Helloworld")
])
@pytest.mark.add
def test_addition(num1,num2,res):
    assert math_file.addition(num1, num2) == res
    assert math_file.addition() == 5
    assert math_file.addition(3) == 7

@pytest.mark.add
def test_addition(num1,num2,res):
    assert math_file.addition(num1, num2) == res
    assert math_file.addition() == 5
    assert math_file.addition(3) == 7


@pytest.mark.add
def test_add_string():
    result = math_file.addition("Hello", "world")
    assert type(result) is str
    assert "Hello" in result

# def test_some():
#    assert 5 == 23

# class TestMath(unittest.TestCase):
#    def test_addition(self):
#        self.assertEqual(math_file.addition(5, 7), 12)
#        self.assertEqual(math_file.addition(5, ), 9)
#        self.assertEqual(math_file.addition(5, 7), 12)
#        self.assertEqual(math_file.addition(), 5)


# if __name__ == "__main__":
# unittest.main()
# test_addition()
# test_add_string()
