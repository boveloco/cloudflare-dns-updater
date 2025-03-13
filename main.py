import requests
import time
import os
import yaml


# Environment variables
IFCONFIG_URL = "https://ifconfig.me"
CLOUDFLARE_ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")
CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
DOMAINS_FILE = os.getenv("DOMAINS_FILE", "domains.yaml")

if not (CLOUDFLARE_ZONE_ID and CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN):
    raise ValueError("Missing required environment variables.")

# Load domains from YAML file
try:
    with open(DOMAINS_FILE, "r") as file:
        DOMAINS = yaml.safe_load(file)
except FileNotFoundError:
    raise FileNotFoundError(f"Domains file '{DOMAINS_FILE}' not found.")
except yaml.YAMLError as e:
    raise ValueError(f"Error parsing YAML file: {e}")

CLOUDFLARE_URL = f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/dns_records"

now = int(time.time())
ip = requests.get(IFCONFIG_URL).text.strip()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}"
}

for d in DOMAINS:
    payload = {
        "content": ip,
        "name": f"{d['name']}",
        "type": "A",
        "comment": f"Update Domain {now}.",
        "ttl": d.get("ttl", 3600),
        "proxied": d.get("proxied", True)
    }
    response = response = requests.request(
        "PATCH", f"{CLOUDFLARE_URL}/{d['id']}", json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Domain {d['name']} was updated correctly.")
    else:
        print(
            f"Error while updating {d['name']}. Error {response.status_code}. \n{response.text}.")
