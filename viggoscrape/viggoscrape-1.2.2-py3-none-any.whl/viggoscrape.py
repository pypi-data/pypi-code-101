"""Scans for assignments on viggo using requests and the POST method."""
import requests
import json

def get_assignments(info):
    data = requests.get(f"https://viggoscrape.xyz/api/v1/scrape?subdomain={info['subdomain']}&username={info['username']}&password={info['password']}")
    return data.json() 

