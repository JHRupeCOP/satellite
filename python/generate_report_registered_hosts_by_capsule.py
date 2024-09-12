#!/usr/bin/env python3

import requests
from collections import defaultdict

# Configuration
# SATELLITE_URL = "https://satellite.conocophillips.net/"
SATELLITE_URL = "https://mariner.conocophillips.net/"
USERNAME = "ruppej"
PASSWORD = ""
# Or use API_TOKEN instead of username/password
API_TOKEN = 'VIy_a3K2rauQivMFaeG_AA'

# Disable warnings for insecure requests (only if using self-signed certificates)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get_json(endpoint):
    url = f"{SATELLITE_URL}/api/v2/{endpoint}"
    # Use either basic auth or token auth
    response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False)
    # response = requests.get(url, headers={'Authorization': f'Bearer {API_TOKEN}'}, verify=False)
    response.raise_for_status()
    return response.json()

def main():
    hosts = get_json('hosts')
    capsules = get_json('smart_proxies')

    capsule_map = {capsule['id']: capsule['name'] for capsule in capsules['results']}
    hosts_by_capsule = defaultdict(list)

    for host in hosts['results']:
        capsule_id = host.get('puppet_proxy_id')
        if capsule_id:
            capsule_name = capsule_map.get(capsule_id, 'Unknown')
            hosts_by_capsule[capsule_name].append(host['name'])

    for capsule, hosts in hosts_by_capsule.items():
        print(f"Capsule Server: {capsule}")
        for host in hosts:
            print(f"  - {host}")
        print()

if __name__ == "__main__":
    main()
