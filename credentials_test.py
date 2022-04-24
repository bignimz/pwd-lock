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

    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account, 'Linkein')
        self.assertEqual(self.new_credential.userName, 'nimrod-musungu')
        self.assertEqual(self.new_credential.password, 'Lkdn@123')

    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


if __name__ == "__main__":
    unittest.main()
