"""
Requests_Part2_APIs.py
Interacting with real REST APIs using requests.
We will use the free JSONPlaceholder API for demonstration.
"""

import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    """Fetch users from the API"""
    print("\n--- GET: Fetching Users ---")
    response = requests.get(f"{BASE_URL}/users")
    
    # Always check if request was successful
    response.raise_for_status() 
    
    users = response.json()
    print(f"Fetched {len(users)} users.")
    for user in users[:3]: # Print first 3
        print(f"ID: {user['id']} | Name: {user['name']} | Email: {user['email']}")

def get_user_posts(user_id):
    """Fetch posts for a specific user using query parameters"""
    print(f"\n--- GET: Fetching Posts for User {user_id} ---")
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
    posts = response.json()
    print(f"User {user_id} has {len(posts)} posts.")
    print(f"First post title: {posts[0]['title']}")

def create_post():
    """Create a new post via POST request"""
    print("\n--- POST: Creating a new Post ---")
    new_post = {
        "title": "Python API Mastery",
        "body": "Learning how to interact with REST APIs.",
        "userId": 1
    }
    
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    print(f"Status Code: {response.status_code} (Created)")
    print("Response data:")
    # json.dumps for pretty printing
    print(json.dumps(response.json(), indent=2))

def update_post(post_id):
    """Update an existing post via PUT request"""
    print(f"\n--- PUT: Updating Post {post_id} ---")
    updated_post = {
        "id": post_id,
        "title": "Updated Title via PUT",
        "body": "This entire resource was replaced.",
        "userId": 1
    }
    
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    print(f"Status Code: {response.status_code}")
    print(f"Updated Title: {response.json().get('title')}")

def delete_post(post_id):
    """Delete a post via DELETE request"""
    print(f"\n--- DELETE: Deleting Post {post_id} ---")
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print(f"Status Code: {response.status_code} (OK/No Content)")

if __name__ == "__main__":
    try:
        get_users()
        get_user_posts(user_id=1)
        create_post()
        update_post(post_id=1)
        delete_post(post_id=1)
    except requests.exceptions.RequestException as e:
        print(f"An API Error occurred: {e}")
