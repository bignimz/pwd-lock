from user import User


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
