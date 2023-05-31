class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def auth(self, entered_password):
        if entered_password == self.password:
            print(f'Hello {self.username}, your password: {self.password}')
            return True
        else:
            return False


def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        user = User(username, password)

        entered_password = input("Password for auth: ")

        if user.auth(entered_password):
            print(f'Authenticate were success! Welcome to company, {username}!')
            break
        else:
            print(f'Authenticate were not success complete')


if __name__ == '__main__':
    login()
