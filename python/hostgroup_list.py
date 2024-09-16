# Imports
import requests
import json
from requests.auth import HTTPBasicAuth
from sat_functions import get_credentials

def get_hostgroups(auth, satellite_url, cert_path):
    # Retreive of hostgroups
    url = f"{satellite_url}/api/hostgroups"
    response = requests.get(url, auth=auth, verify=cert_path)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"Failed to get content views: {response.status_code} - {response.text}")    

def main():
    satellite_url = "https://satellite.conocophillips.net"
    cert_path = "/etc/pki/tls/certs/ca-bundle.crt"

    # Get user credentials
    username, password = get_credentials()
    auth = HTTPBasicAuth(username, password)

    host_groups = get_hostgroups(auth, satellite_url, cert_path)

    print(json.dumps(host_groups, indent=4))

if __name__ == "__main__":
    main()    
 
