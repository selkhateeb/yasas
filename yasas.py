import getpass

def ask_for_creds():
    username = input('Username: ')
    password = getpass.getpass()

    return (username, password)

if __name__ == '__main__':
    print(ask_for_creds())