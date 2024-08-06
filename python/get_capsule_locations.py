#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import getpass

# Constants
# SATELLITE_URL = "https://satellite.conocophillips.net/"
CERT_PATH = "/etc/pki/tls/certs/ca-bundle.crt"
satellite_host = "satellite.conocophillips.net"

# Function to get the Satellite API URL
def get_api_url(satellite_host):
    return f"https://{satellite_host}/api/v2"

# Function to get the list of capsule servers
def get_capsules(satellite_host, username, password):
    url = f"{get_api_url(satellite_host)}/smart_proxies"
    response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=CERT_PATH)
    response.raise_for_status()
    return response.json()

# Function to get the list of locations
def get_locations(satellite_host, username, password):
    url = f"{get_api_url(satellite_host)}/locations?per_page=1000"
    response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=CERT_PATH)
    response.raise_for_status()
    return response.json()

# Function to get the capsules associated with each location
def get_location_capsules(satellite_host, username, password, location_id):
    url = f"{get_api_url(satellite_host)}/locations/{location_id}/smart_proxies"
    response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=CERT_PATH)
    response.raise_for_status()
    return response.json()

# Main function
def main():
    # satellite_host = input("Enter the Red Hat Satellite hostname or IP: ")
    username = input("Enter your Satellite username: ")
    password = getpass.getpass("Enter your Satellite password: ")

    try:
        capsules = get_capsules(satellite_host, username, password)
        locations = get_locations(satellite_host, username, password)

        print("\nCapsule Servers:")
        for capsule in capsules['results']:
            print(f"ID: {capsule['id']}, Name: {capsule['name']}, URL: {capsule['url']}")

        print("\nLocations and Associated Capsules:")
        for location in locations['results']:
            print(f"\nLocation: {location['name']}")
            location_capsules = get_location_capsules(satellite_host, username, password, location['id'])
            if location_capsules['results']:
                for capsule in location_capsules['results']:
                    print(f"  - Capsule ID: {capsule['id']}, Name: {capsule['name']}, URL: {capsule['url']}")
            else:
                print("  No associated capsules")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
