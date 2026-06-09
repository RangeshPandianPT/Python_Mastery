"""
Requests_Part1_Advanced.py
Advanced techniques for using the `requests` library in Python.
"""

import requests
from requests.auth import HTTPBasicAuth
import time

def main():
    print("=== ADVANCED REQUESTS ===")

    # 1. Using Query Parameters
    print("\n--- 1. Query Parameters (GET) ---")
    url = "https://httpbin.org/get"
    params = {'search': 'python', 'page': 2}
    response = requests.get(url, params=params)
    print(f"URL Requested: {response.url}")
    print(f"Arguments parsed by server: {response.json().get('args')}")

    # 2. Setting Headers
    print("\n--- 2. Custom Headers ---")
    headers = {
        'User-Agent': 'Python_Mastery_Bot/1.0',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(f"Headers sent: {response.json().get('headers').get('User-Agent')}")

    # 3. HTTP POST Requests (Sending JSON data)
    print("\n--- 3. POST Requests (JSON) ---")
    post_url = "https://httpbin.org/post"
    payload = {'username': 'admin', 'password': 'supersecret'}
    # Use the 'json' parameter to automatically set headers and encode dict to json
    post_response = requests.post(post_url, json=payload)
    print(f"Status Code: {post_response.status_code}")
    print(f"JSON returned by server: {post_response.json().get('json')}")

    # 4. Authentication
    print("\n--- 4. Basic Authentication ---")
    auth_url = "https://httpbin.org/basic-auth/user/pass"
    auth_response = requests.get(auth_url, auth=HTTPBasicAuth('user', 'pass'))
    print(f"Auth Success (Status): {auth_response.status_code}")

    # 5. Session Objects (Persisting Cookies/Headers)
    print("\n--- 5. Requests Sessions ---")
    # Sessions allow you to persist certain parameters across requests
    with requests.Session() as session:
        session.headers.update({'x-test-header': 'session-persistent-value'})
        
        # Setting a cookie
        session.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
        
        # Retrieving the cookie in a subsequent request
        cookie_resp = session.get("https://httpbin.org/cookies")
        print(f"Cookies from Session: {cookie_resp.json().get('cookies')}")

if __name__ == "__main__":
    main()
