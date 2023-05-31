from cryptography.fernet import Fernet
import json
import os

def generate_key():

  # Generates a new Fernet key and saves it in a file with the name "key.key".
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():

  # Loads the previously generated Fernet key from the file "key.key".
    return open("key.key", "rb").read()

def add_password(service_name, username, password):

  # Adds a new password to the passwords file.
    data = {}
    file_name = "passwords.json"

    if os.path.exists(file_name):
        with open(file_name, "r") as password_file:
            data = json.load(password_file)

    data[service_name] = {"username": username, "password": password}

    with open(file_name, "w") as password_file:
        json.dump(data, password_file)

def new_password():
 
# Ask the user for a new password and save it.
    service = input("Service name: ")
    username = input("Username: ")
    password = input("Password: ")

    key = load_key()
    encoded_password = password.encode()

    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password).decode()

    add_password(service, username, encrypted_password)

    print("Password added successfully!")

def retrieve_password(service_name):

  # Retrieves the password for a given service from the passwords file.
    with open("passwords.json", "r") as file:
        data = json.load(file)

    if service_name in data:
        key = load_key()
        encrypted_password = data[service_name]["password"].encode()

        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password).decode()

        print(f"Service: {service_name}")
        print(f"Username: {data[service_name]['username']}")
        print(f"Password: {decrypted_password}")
    else:
        print(f"No password found for service '{service_name}'.")

def display_menu():

  # Displays the main menu for the password manager.
    print("Password Manager")
    print("1. Retrieve password")
    print("2. Add new password")
    print("3. Exit")

def main():

  # Displays the main menu and handles user input.
    if not os.path.exists("key.key"):
        generate_key()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            retrieve_password(service)
        elif choice == "2":
            new_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
