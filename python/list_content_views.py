#!/usr/bin/env python3

#imports
from sat_functions import get_credentials, get_content_views
import requests
from requests.auth import HTTPBasicAuth

def main():
    # Get user credentials
    username, password = get_credentials()
    auth = HTTPBasicAuth(username, password)

    # Get content views
    content_views = get_content_views(auth)

    # Iterate over content views and print details
    for cv in content_views:
        print(f"\nContent View: {cv['name']} (ID: {cv['id']}) (composite: {cv['composite']})")

if __name__ == "__main__":
    main()
    
