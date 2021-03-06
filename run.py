# Run python3.8 run.py

from user import User
from credentials import Credentials


def create_new_user(username, password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()


def display_user():
    """
    Function to display existing user
    """
    return User.display_user()


def login_user(username, password):
    """
    function that checks whether a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credential(account, userName, password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    return credentials.save_credentials()


def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)


def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):
    """
    Copy password to clipboard using the pyperclip
    """
    return Credentials.copy_password(account)


def passlocker():
    print("Hello Welcome to Password Locker...\n Choose a shortcode to proceed.\n CA ---  To Create New Account  \n LI ---  If You Have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Create Account")
        print('*' * 50)
        username = input("Enter Username: ")
        while True:
            print(" OP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'op':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username, password))
        print("*"*85)
        print(
            f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        print("Enter your User name and your Password to log in:")
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Your PassWord Locker Account")
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(
                    " =EP - To enter your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'ep':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(
                account, userName, password))
            print('\n')
            print(
                f"Account Credential for: {account} - UserName: {userName} - Password:{password} was succesfully created")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")

                for account in display_accounts_details():
                    print(
                        f" Account:{account.account} \n User Name:{username}\n Password:{password}")
            else:
                print("No Credentials saved yet")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")

                print(
                    f"User Name: {search_credential.userName} Password :{search_credential.password}")

            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)

                search_credential.delete_credentials()
                print('\n')
                print(
                    f"Credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print(
                    "The deleted credential does not exist in the credential list")

        elif short_code == 'gp':

            password = generate_Password()
            print(
                f" {password} Has been generated succesfully")
        elif short_code == 'ex':
            print("Thanks for using Password Locker..!")
            break
        else:
            print(
                "Wrong entry, Please enter the right option")
    else:
        print("Please enter a valid input to continue")


if __name__ == '__main__':
    passlocker()
