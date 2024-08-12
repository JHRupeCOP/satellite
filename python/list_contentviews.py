#!/usr/bin/env python3

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

def get_lifecycle_environments(auth):
    """Get a list of all lifecycle environments."""
    url = f"{SATELLITE_URL}/katello/api/environments"
    response = requests.get(url, auth=auth, verify=CERT_PATH)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to get lifecycle environments: {response.status_code} - {response.text}")

def get_content_view_versions(auth, content_view_id):
    """Get a list of all versions of a content view."""
    url = f"{SATELLITE_URL}/katello/api/content_views/{content_view_id}/content_view_versions"
    response = requests.get(url, auth=auth, verify=CERT_PATH)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to get content view versions: {response.status_code} - {response.text}")

def main():
    # Get user credentials
    username, password = get_credentials()
    auth = HTTPBasicAuth(username, password)

    # Get content views
    content_views = get_content_views(auth)
    
    # Get lifecycle environments
    lifecycle_environments = get_lifecycle_environments(auth)
    lifecycle_envs_map = {env['id']: env['name'] for env in lifecycle_environments}

    # Iterate over content views and print details
    for cv in content_views:
        print(f"\nContent View: {cv['name']} (ID: {cv['id']})")
        
        # Get content view versions
        versions = get_content_view_versions(auth, cv['id'])
        
        for version in versions:
            env_name = lifecycle_envs_map.get(version['environment_id'], "Unknown")
            print(f"  Version: {version['version']}")
            print(f"  Lifecycle Environment: {env_name}")
            print(f"  Published At: {version['created_at']}")
            print(f"  Last Published At: {version['updated_at']}")

if __name__ == "__main__":
    main()
