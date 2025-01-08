import os
import hashlib
import getpass
import win32security
import pyotp
import time

class SecureSteps:
    def __init__(self):
        self.users = {}
        self.otp_secrets = {}

    def create_user(self, username, password):
        salt = os.urandom(32)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        self.users[username] = (salt, pwd_hash)
        self.otp_secrets[username] = pyotp.random_base32()

    def verify_user(self, username, password):
        if username not in self.users:
            return False
        salt, stored_hash = self.users[username]
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return pwd_hash == stored_hash

    def generate_otp(self, username):
        if username in self.otp_secrets:
            totp = pyotp.TOTP(self.otp_secrets[username])
            return totp.now()
        return None

    def verify_otp(self, username, otp):
        if username in self.otp_secrets:
            totp = pyotp.TOTP(self.otp_secrets[username])
            return totp.verify(otp)
        return False

def main():
    security = SecureSteps()
    print("SecureSteps: Enhanced Security for Windows Logins")

    while True:
        print("\n1. Create User\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            security.create_user(username, password)
            print(f"User {username} created successfully.")

        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            if security.verify_user(username, password):
                print("Password verified. Generating OTP...")
                otp = security.generate_otp(username)
                print(f"Your OTP is: {otp}")
                user_otp = input("Enter the OTP: ")
                
                if security.verify_otp(username, user_otp):
                    print("Login successful!")
                else:
                    print("Invalid OTP.")
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Exiting SecureSteps.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()