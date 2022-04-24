from user import User
import random
import string
import pyperclip


class Credentials:
    """"
    Create credentials class that generates credentials object blueprint
    """

    credentials_list = []

    @classmethod
    def verify_user(cls, username, password):
        """
        Method to verify if user is available or not in the users list
        """
        user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                user == user.username
                return user

    def __init__(self, account, userName, password):
        """"
        Method to define the user credentials
        """
        self.account = account
        self.userName = userName
        self.password = password

    def save_credentials(self):
        """"
        Method to store account credentials from credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        Method to deletes account credentials from credentials list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list
