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

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Gmail", "alroude", "pass@123")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Gmail", "alroude", "pass@123")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("Gmail", "alroude", "pass@123")
        test_credential.save_details()

        the_credential = Credentials.find_credential("Gmail")

        self.assertEqual(the_credential.account, test_credential.account)

    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        the_credential = Credentials("Gmail", "alroude", "pass@123")
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Gmail")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()
