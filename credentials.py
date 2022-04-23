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
