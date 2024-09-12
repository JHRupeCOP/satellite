#!/usr/bin/env python3

# Imports
import requests
from requests.auth import HTTPBasicAuth
import getpass

# Constants
SATELLITE_URL = "https://satellite.conocophillips.net"
CERT_PATH = "/etc/pki/tls/certs/ca-bundle.crt"

def get_credentials():
    """Prompt the user for credentials."""
    username = input("Enter your Satellite username: ")
    password = getpass.getpass("Enter your Satellite password: ")
    return username, password

def get_content_views(auth):
    """Get a list of all content views."""
    url = f"{SATELLITE_URL}/katello/api/content_views"
    response = requests.get(url, auth=auth, verify=CERT_PATH)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to get content views: {response.status_code} - {response.text}")
