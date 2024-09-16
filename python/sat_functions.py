# Imports
import requests
import sys
from requests.auth import HTTPBasicAuth
import getpass

def get_credentials():
    """Prompt the user for credentials."""
    username = input("Enter your Satellite username: ")
    password = getpass.getpass("Enter your Satellite password: ")
    return username, password

def get_content_views(auth):
    """Get a list of all content views."""
    url = f"{satellite_url}/katello/api/content_views"
    response = requests.get(url, auth=auth, verify=cert_path)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to get content views: {response.status_code} - {response.text}")

def show_main_menu():
    print("\nSelect a Satellite server to connect to")
    print("1. Production - (bvlusatp0001)")
    print("2. Development - (bvluapd0382)")
    print("3. Legacy - (mariner)")
    print("9. quit")
   
def menu_selection(option, satellite_url, cert_path):
    cert_path = "/etc/pki/tls/certs/ca-bundle.crt"
    if option == "1":
        satellite_url = "https://satellite.conocophillips.net"
        return satellite_url, cert_path, False
    elif option == "2":
        satellite_url = "https://satellite-dev.conocophillips.net/"
        return satellite_url, cert_path, False
    elif option == "3":
        satellite_url = "https://mariner.conocophillips.net/"
        cert_path = False
        return satellite_url, cert_path, False
    elif option == "9":
        print("\nExiting\n")
        sys.exit()
        # satellite_url = "exit"
        # cert_path = None
        # return satellite_url, cert_path, False
    else:    
        print("Invalid option. Please choose again.")
        satellite_url = None
        cert_path = None
        return satellite_url, cert_path, True
    
