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
