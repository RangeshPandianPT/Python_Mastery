# Introduction to requests
# The requests library makes HTTP requests in Python simple.

import requests
import json

print("--- 1. Making a Simple GET Request ---")
# Fetching data from a public API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful
if response.status_code == 200:
    print("Request Successful!")
    print(f"Status Code: {response.status_code}")
    
    # Parse the JSON response
    data = response.json()
    print("\nResponse Data:")
    print(json.dumps(data, indent=4))
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

print("\n--- 2. Making a Request with Parameters ---")
# Adding query parameters to a GET request
params = {'userId': 1}
response_with_params = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
if response_with_params.status_code == 200:
    posts = response_with_params.json()
    print(f"Fetched {len(posts)} posts for user 1.")

print("\n--- 3. Making a POST Request ---")
# Sending data to an API
new_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
headers = {'Content-type': 'application/json; charset=UTF-8'}

post_response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post, headers=headers)
print(f"POST Response Status: {post_response.status_code}")
print("Created Data:")
print(json.dumps(post_response.json(), indent=4))
