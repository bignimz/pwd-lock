class User:
    """"
    Create user class that generates new user

    """

    user_list = []

    def __init__(self, username, password):
        """"
        Initializing the user properties
        """
        self.username = username
        self.password = password

    def save_user(self):
        """"
        Method to save new user in the users list
        """
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        """"
        Method that deletes a saved user from the users list
        """
        User.user_list.remove(self)
