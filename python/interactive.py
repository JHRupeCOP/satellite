#!/usr/bin/env python3

#imports
import requests
from requests.auth import HTTPBasicAuth
from sat_functions import get_credentials, get_content_views, show_menu, menu_selection

def main():
    satellite_url = None
    cert_path = None
    running = True
    while running:
        show_main_menu()
        choice = input("Enter your choice:")
        satellite_url, cert_path, running = menu_selection(choice, satellite_url, cert_path)   
        
    print(satellite_url, cert_path)   
    exit()

    # Get user credentials
    username, password = get_credentials()
    auth = HTTPBasicAuth(username, password)


if __name__ == "__main__":
    main()
    
