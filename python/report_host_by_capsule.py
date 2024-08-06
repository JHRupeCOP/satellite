#!/usr/bin/env python3

import requests
import json
from collections import defaultdict
import getpass

# Replace this variable with your actual Satellite server URL
SATELLITE_URL = "https://satellite.conocophillips.net/"
API_URL = f"{SATELLITE_URL}/api/v2"
CERT_PATH = "/etc/pki/tls/certs/ca-bundle.crt"

# Function to get all hosts
def get_all_hosts(session):
    url = f"{API_URL}/hosts"
    response = session.get(url)
    response.raise_for_status()
    return response.json()['results']

# Function to get details of a specific host
def get_host_details(session, host_id):
    url = f'{API_URL}/hosts/{host_id}'
    response = session.get(url)
    response.raise_for_status()
    return response.json()

# Function to group hosts by capsule server
def group_hosts_by_capsule(hosts):
    grouped_hosts = defaultdict(list)
    for host in hosts:
        host_id = host['id']
        details = get_host_details(session, host_id)
        capsule_name = details['host']['subscription']['capsule']['name']
        grouped_hosts[capsule_name].append(details['host']['name'])
    return grouped_hosts

# Prompt for credentials
username = input("Enter your Satellite username: ")
password = getpass.getpass("Enter your Satellite password: ")

# Create a session with authentication
session = requests.Session()
session.auth = (username, password)
session.verify = CERT_PATH  # Set to True if using a proper SSL certificate

# Get all hosts
hosts = get_all_hosts(session)

# Group hosts by capsule server
grouped_hosts = group_hosts_by_capsule(hosts)

# Print grouped hosts
for capsule, hosts in grouped_hosts.items():
    print(f'Capsule: {capsule}')
    for host in hosts:
        print(f'  Host: {host}')
