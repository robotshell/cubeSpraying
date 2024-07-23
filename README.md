<h1 align="center">
  <br>
  <a href="https://github.com/robotshell/cubeSpraying"><img src="https://i.ibb.co/9w6wcmG/logo-1.png" alt="cubeSpraying" style="width:100%"></a>
</h1>

cubeSpraying performs a Password Spraying attack against a Roundcube Webmail application. Password Spraying is a technique where an attacker attempts one password against many users to avoid being locked out due to multiple failed login attempts.

## Description

cubeSpraying attempts to log in to Roundcube Webmail using a list of usernames and a list of passwords. Various parameters can be specified to adjust the script's behavior, including a verbose mode and a timeout between login attempts.

### Key Features

- **Password spraying**: Attempts one password against multiple users before moving to the next password.
- **Verbose mode**: Displays details of each login attempt.
- **Timeout**: Allows specifying a wait time between each login attempt.
- **Session handling**: Uses `requests` sessions to handle cookies and authentication tokens.
- **Flexible input**: Accepts either a single value or a file containing multiple values for both usernames and passwords.

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
    git clone https://github.com/robotshell/cubeSpraying.git
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
python cubeSpraying.py --url URL --usernames USERNAMES --passwords PASSWORDS [--verbose] [--timeout TIMEOUT]
```
# Disclaimer
This tool is intended for educational and research purposes only. The author and contributors are not responsible for any misuse of this tool. Users are advised to use this tool responsibly and only on systems for which they have explicit permission. Unauthorized access to systems, networks, or data is illegal and unethical. Always obtain proper authorization before conducting any kind of activities that could impact other users or systems.
