import bcrypt
import csv

input_username = ""
input_password = ""
hashed_password = ""

def prompt():
    global input_username
    global input_password
    global hashed_password
    input_username = input("Unique Username: ").strip()
    input_password = input("Password: ")
    hashed_password = bcrypt.hashpw(input_password.encode("utf-8"), bcrypt.gensalt())

def authenticate(username, password):
    with open('auth.csv', 'r') as auth:
        reader = csv.reader(auth)
        for row in reader:
            if row[0] == username:
                if bcrypt.checkpw(password.encode("utf-8"), row[1].encode("utf-8")):
                    return (True, "Login successful")
                else:
                    return (False, "Invalid Credentials")
        return (False, "Account doesn't exist")

def check_account(username):
    with open('auth.csv', 'r') as auth:
        reader = csv.reader(auth)
        for row in reader:
            if row[0] == username:
                return True
        return False

def add_to_csv(username, password):
    checker = check_account(username)
    if not checker:
        with open('auth.csv', 'a+') as auth:
            writer = csv.writer(auth, delimiter=',',lineterminator='\n')
            writer.writerow([username, password.decode("utf-8")])
            return True
    else:
        return False


def register():
    prompt()
    added = add_to_csv(input_username, hashed_password)
    if(added):
        print("\nRegistration successful")
    else:
        print("\nUsername already exists")

def login():
    prompt()
    (checker, msg) = authenticate(input_username, input_password)
    print(f"\n{msg}")
    return checker