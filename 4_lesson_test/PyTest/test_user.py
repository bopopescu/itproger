import unittest
import user
import pytest


class TestUser(unittest.TestCase):
    # Запускаеться перед началом
    def setUp(self):
        self.obj = user.User()

    def test_init(self):
        alex = user.User("Alex", 25)
        self.assertEqual(alex.name, "Alex")
        self.assertEqual(alex.age, 25)

        bob = user.User("Bob")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.age, 35)

        self.assertEqual(self.obj.name, "bot")
        self.assertEqual(self.obj.age, 35)

    def test_print_all(self):
        self.assertEqual(self.obj.print_all(), "bot возрастом 35")

    @pytest.mark.slow
    def test_print_to_file(self):
        self.obj.print_to_file("text.txt")
        result = self.obj.read_from_file("text.txt")
        self.assertEqual(result, self.obj.print_all())

    # Запускаеться после завершения теста


if __name__ == "__main__":
    unittest.main()
