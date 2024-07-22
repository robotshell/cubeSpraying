# cubeSpraying

cubeSpraying performs a Password Spraying attack against a Roundcube Webmail application. Password Spraying is a technique where an attacker attempts one password against many users to avoid being locked out due to multiple failed login attempts.

## Description

cubeSpraying attempts to log in to Roundcube Webmail using a list of usernames and a list of passwords. Various parameters can be specified to adjust the script's behavior, including a verbose mode and a timeout between login attempts.

### Key Features

- **Password Spraying**: Attempts one password against multiple users before moving to the next password.
- **Verbose Mode**: Displays details of each login attempt.
- **Timeout**: Allows specifying a wait time between each login attempt.
- **Session Handling**: Uses `requests` sessions to handle cookies and authentication tokens.
- **Flexible Input**: Accepts either a single value or a file containing multiple values for both usernames and passwords.

### Flexible Input Options

cubeSpraying can take either a single value or a file containing multiple values for both usernames and passwords:

- **Usernames**: You can pass a single username or a file containing a list of usernames, one per line.
- **Passwords**: You can pass a single password or a file containing a list of passwords, one per line.

This flexibility allows for easy and quick testing with single credentials as well as comprehensive testing with large lists of usernames and passwords.

## Requirements

- Python 3.x
- Libraries: `requests`

## Installation

1. Clone this repository or download the files.

    ```sh
    git clone [https://github.com/your_username/your_repository.git](https://github.com/robotshell/cubeSpraying.git)
    ```

2. Navigate to the project directory.

    ```sh
    cd cubeSpraying
    ```

3. Install the `requests` library if you don't have it installed.

    ```sh
    pip install requests
    ```

## Usage

Run the script with the following parameters:

```sh
python script.py --url URL --usernames USERNAMES --passwords PASSWORDS [--verbose] [--timeout TIMEOUT]
