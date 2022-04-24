import unittest
from user import User
from credentials import Credentials


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('alroude', 'Alroude123')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, 'alroude')
        self.assertEqual(self.new_user.password, 'Alroude123')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
