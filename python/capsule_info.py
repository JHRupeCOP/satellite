#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

# Constants
SATELLITE_API_URL = "https://satellite.conocophillips.net/api/v2"

def get_credentials():
    username = input("Enter your Satellite username: ")
    password = input("Enter your Satellite password: ")
    return username, password

def get_capsules(api_url, auth):
    headers = {'Content-Type': 'application/json'}
    capsules_url = f"{api_url}/smart_proxies"
    response = requests.get(capsules_url, auth=auth, headers=headers)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Failed to retrieve capsules: {response.status_code}")
        return []

def list_features_and_locations(api_url, capsule, auth):
    headers = {'Content-Type': 'application/json'}

    # Get enabled features
    features_url = f"{api_url}/smart_proxy/{capsule['id']}/features"
    response = requests.get(features_url, auth=auth, headers=headers)
    if response.status_code == 200:
        features = response.json()
        print(f"\nEnabled Features for Capsule '{capsule['name']}' (ID: {capsule['id']}):")
        for feature in features:
            print(f" - {feature['name']}")
    else:
        print(f"Failed to retrieve features for Capsule '{capsule['name']}': {response.status_code}")

    # Get associated locations
    locations_url = f"{api_url}/capsules/{capsule['id']}/locations"
    response = requests.get(locations_url, auth=auth, headers=headers)
    if response.status_code == 200:
        locations = response.json()
        print(f"\nAssociated Locations for Capsule '{capsule['name']}' (ID: {capsule['id']}):")
        for location in locations:
            print(f" - {location['name']}")
    else:
        print(f"Failed to retrieve locations for Capsule '{capsule['name']}': {response.status_code}")

def main():
    username, password = get_credentials()
    auth = HTTPBasicAuth(username, password)
    
    capsules = get_capsules(SATELLITE_API_URL, auth)
    if not capsules:
        print("No capsules found or unable to retrieve capsules.")
        return

    for capsule in capsules:
        list_features_and_locations(SATELLITE_API_URL, capsule, auth)

if __name__ == "__main__":
    main()
