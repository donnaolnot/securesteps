# SecureSteps

SecureSteps is a Python-based program designed to enhance security measures during login and authentication processes on Windows systems. This tool implements password hashing and time-based one-time password (TOTP) verification to ensure secure access to user accounts.

## Features

- **User Creation**: Create a new user with a secure password.
- **Password Hashing**: Passwords are hashed with a unique salt using PBKDF2-HMAC-SHA256.
- **TOTP Generation**: Generate a time-based one-time password for two-factor authentication.
- **User Authentication**: Verify user credentials and OTP for secure login.

## Installation

1. **Pre-requisites**: Ensure you have Python 3.x installed on your system.
2. **Libraries**: The program requires `pyotp` and `pywin32` libraries. You can install them using pip:

   ```bash
   pip install pyotp pywin32
   ```

3. **Run the Program**: Execute the script in your terminal or command prompt:

   ```bash
   python secure_steps.py
   ```

## Usage

1. **Create a User**: Follow the prompts to create a new user with a username and password.
2. **Login**: Enter your credentials and follow the prompts to enter the OTP for successful authentication.
3. **Exit**: Choose the exit option to close the program.

## Security Considerations

- Ensure the environment where this program runs is secure.
- Regularly update your password for enhanced security.
- Keep your OTP secret secure and do not share it with unauthorized individuals.

## License

This project is open-source and available under the MIT License. Feel free to contribute or modify as necessary for your needs.