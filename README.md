# PASSWORD LOCKER

This is an application that is build purely on Python 3.8 that requires a user to safely create a master account in the application and start creating and saving other accounts credentials such as username and Password of other social media accounts they posses. 

This Application is just a prototype and does not have any database to store the credentials, and as such, all the saved credentials are lost once the application is restarted. 


## Technologies Implemented in this Project

1. PYTHON v3.8
2. PyperClip
3. MARKDOWN for Documentation
4. Unit Test (For Testing the Application)

## Project Author

Name: Nimrod Musungu <br>
Email: nimrod.chitayi@gmail.com<br>
Website: nimrodmusungu.com




## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./interface.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```cp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```D```| The application exits|

## Installation

Use the SSH to clone this repo in your local machine.

```bash
git@github.com:bignimz/pwd-lock.git
```

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:
  ```bash
  $ python3.8 run.py
  ```

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
