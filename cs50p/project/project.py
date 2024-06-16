from pyfiglet import Figlet
import pyfiglet
from pwinput import pwinput
import string
import pandas as pd
import os
import hashlib

ALPHABET = string.ascii_letters + string.digits


def master_password_get():
    """
    Retrieves the master password from the user and returns it as an integer.

    If the 'password_hash.txt' file does not exist, the user is prompted to enter a master password.
    The entered password is processed by replacing alphabetic characters with their corresponding ASCII values.
    The processed password is then hashed using SHA256 and stored in the 'password_hash.txt' file.
    The processed password, with hyphens removed, is returned as an integer.

    If the 'password_hash.txt' file exists, the stored hash is read from the file.
    The user is prompted to enter the master password, which is processed and hashed.
    If the hashed password matches the stored hash, the processed password is returned as an integer.
    Otherwise, the user is prompted to try again until the correct password is entered.
    """

    if not os.path.exists("password_hash.txt"):
        master_pass = pwinput(prompt="\nEnter master password: ", mask="*")
        processed_password = ""
        for char in master_pass:
            if char.isalpha():
                processed_password += str(ord(char.lower()) - 96)
            else:
                processed_password += char
        master_pass_hash = hashlib.sha256(processed_password.encode()).hexdigest()
        with open("password_hash.txt", "w") as file:
            file.write(master_pass_hash)
        return int(processed_password.replace("-", ""))
    else:
        with open("password_hash.txt", "r") as file:
            stored_hash = file.read().strip()
        while True:
            master_pass = pwinput(prompt="\nEnter master password: ", mask="*")
            processed_password = ""
            for char in master_pass:
                if char.isalpha():
                    processed_password += str(ord(char.lower()) - 96)
                else:
                    processed_password += char
            master_pass_hash = hashlib.sha256(processed_password.encode()).hexdigest()
            if master_pass_hash == stored_hash:
                return int(processed_password.replace("-", ""))
            else:
                print("Incorrect password. Try again.")


def encrypt_password(master, password):
    """
    Encrypts the given password using the provided master key.

    Parameters:
    - master (int): The master key used for encryption.
    - password (str): The password to be encrypted.

    Returns:
    - str: The encrypted password.
    """
    print(password, master)
    encrypted_pass = ""
    for char in password:
        if char in ALPHABET:
            new_pos = (ALPHABET.find(char) + master) % len(ALPHABET)
            encrypted_pass += ALPHABET[new_pos]
        else:
            encrypted_pass += char
    return encrypted_pass


def decrypt_password(password, master):
    """
    Decrypts a password using a given master key.

    Parameters:
    password (str): The password to be decrypted.
    master (int): The master key used for decryption.

    Returns:
    str: The decrypted password.
    """
    decrypted_pass = ""
    for char in password:
        if char in ALPHABET:
            new_pos = (ALPHABET.find(char) - master) % len(ALPHABET)
            decrypted_pass += ALPHABET[new_pos]
        else:
            decrypted_pass += char
    return decrypted_pass


def create_csv():
    data = {"Url/App name": [], "Username": [], "Password": []}
    df = pd.DataFrame(data)
    df.to_csv("password.csv", index=False)


def add_new_password(name, password, url):
    password_data = {"Url/App name": [url], "Username": [name], "Password": [password]}
    df = pd.DataFrame(password_data)
    df.to_csv("password.csv", mode="a", header=False, index=False)
    return df.to_csv().split(",")[-3:]


def search(url="", master_password=0):
    df = pd.read_csv("password.csv")
    dfS = df[df["Url/App name"].str.contains(url, na=False, case=False)]
    index_d = dfS.index.values
    password = []
    dfS = dfS.reset_index()
    for index, row in dfS.iterrows():
        find_password = dfS.loc[index, "Password"]
        dec_password = decrypt_password(find_password, master_password)
        password.append(dec_password)
    dfS = dfS.set_index(index_d)
    dfS["Password"] = password
    return dfS


def edit_password(index, new_name, new_password):
    df = pd.read_csv("password.csv")
    df.loc[index, ["Username", "Password"]] = [new_name, new_password]
    df.to_csv("password.csv", index=False)


def delete_password(index):
    df = pd.read_csv("password.csv")
    df.drop([index], axis=0, inplace=True)
    df.to_csv("password.csv", index=False)


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    data_file = os.path.isfile("password.csv")
    if not data_file:
        create_csv()
    title = pyfiglet.figlet_format("Pass-Man")
    try:
        while True:
            print(title)
            try:
                master_password = master_password_get()
                break
            except ValueError:
                print("\n WARNING: MASTER PASSWORD CONSISTS OF LETTERS & NUMBERS ONLY.")
            except KeyboardInterrupt:
                print("\n" * 2 + " THANK YOU")
                break
        while True:
            print(
                "\n" * 3
                + " [01] ADD NEW CREDENTIAL\
                    \n\n [02] SEARCH CREDENTIAL\
                    \n\n [03] EDIT CREDENTIAL\
                    \n\n [04] DELETE CREDENTIAL\
                        \n\n [05] EXIT"
            )
            menu_option = int(input("\n" * 3 + " SELECT AN OPTION & PRESS ENTER : "))
            if menu_option == 1:
                clear()
                name = input("\n ENTER NAME/USERNAME YOU WANT TO SAVE -- ")
                password = pwinput(
                    prompt="\n ENTER PASSWORD YOU WANT TO SAVE -- ", mask="*"
                )
                url = input("\n ENTER URL/APP NAME YOU WANT TO SAVE -- ")
                if name == "" or password == "" or url == "":
                    print("\n" * 2 + " WARNING: ALL FIELDS ARE REQUIRED")
                encrypted_password = encrypt_password(master_password, password)
                print(encrypted_password)
                add_new_password(name, encrypted_password, url)
                print("\n" * 2 + " PASSWORD SAVED SUCCESSFULLY")
            elif menu_option == 2:
                clear()
                url = input("\n ENTER URL/APP NAME YOU WANT TO SEARCH : ")
                search(url, master_password)
                print("\n" * 2 + " SEARCH RESULTS")
                in_mkdwn = search(url, master_password).to_markdown(
                    tablefmt="orgtbl", index=False
                )
                print("\n" + in_mkdwn)
            elif menu_option == 3:
                clear()
                print("\n" * 2 + " SEARCH CREDENTIAL TO EDIT")
                url = input("\n ENTER URL/APP NAME YOU WANT TO EDIT : ")
                res = search(url)
                show_in_md = res.to_markdown(tablefmt="orgtbl", index=False)
                print("\n" + show_in_md)
                print("\n" * 2 + "-" * 50)
                if len(res) > 0:
                    index = int(input("\n ENTER INDEX OF CREDENTIAL TO EDIT : "))
                    new_name = input("\n ENTER NEW NAME/USERNAME : ")
                    new_password = pwinput(prompt="\n ENTER NEW PASSWORD : ", mask="*")
                    if new_name == "" or new_password == "":
                        print("\n" * 2 + " WARNING: ALL FIELDS ARE REQUIRED")
                    encrypted_password = encrypt_password(master_password, new_password)
                    edit_password(index, new_name, encrypted_password)
                    print("\n" * 2 + " EDITED SUCCESSFULLY")
            elif menu_option == 4:
                clear()
                print("\n" * 2 + " SEARCH CREDENTIAL TO DELETE")
                url = input("\n ENTER URL/APP NAME YOU WANT TO DELETE : ")
                res = search(url)
                show_in_md = res.to_markdown(tablefmt="orgtbl", index=False)
                print("\n" + show_in_md)
                print("\n" * 2 + "-" * 50)
                if len(res) > 1:
                    index = int(input("\n ENTER INDEX OF CREDENTIAL TO DELETE : "))
                    delete_password(index)
                    print("\n" * 2 + " DELETED SUCCESSFULLY")
            elif menu_option == 5:
                print("\n" * 2 + " THANK YOU")
                break
    except KeyboardInterrupt:
        print("\n" * 2 + " THANK YOU")


if __name__ == "__main__":
    main()
