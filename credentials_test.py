import unittest
from user import User
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """

    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials(
            'Linkedin', 'nimrod-musungu', 'Lkdn@123')


if __name__ == "__main__":
    unittest.main()
