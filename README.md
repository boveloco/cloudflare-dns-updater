# DNS Updater

This project updates DNS records on Cloudflare using the Cloudflare API. It fetches the current public IP address and updates the DNS records for specified domains.

## Behaviour
Python code will get the current public IP address on `ifconfig.me` and will update the DNS records configured in the file `domains.yaml`.
All of those domains will get the same IP address.

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dns-updater.git
    cd dns-updater
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Setup required environment variables:
    ```sh
    export CLOUDFLARE_API_TOKEN="your_cloudflare_api_token"
    export CLOUDFLARE_ZONE_ID="your_cloudflare_zone_id"
    export CLOUDFLARE_ACCOUNT_ID="your_cloudflare_account_id"
    ```
4. Setup domains.yaml file with the following format:
    ```yaml
    - name: vpn.nullservers.com
      id: 0dbadc4e75dd23227baa91d6a92dce14
      proxied: false
      location: home
    ```
5. Run the script:
    ```sh
    python main.py
    ```
## Docker image is available in the repository

```bash
docker pull ghcr.io/nullservers/dns-updater:latest
docker run -e CLOUDFLARE_API_TOKEN="your_cloudflare_api_token" \ 
           -e CLOUDFLARE_ZONE_ID="your_cloudflare_zone_id" \
           -e CLOUDFLARE_ACCOUNT_ID="your_cloudflare_account_id" \
           -v /path/to/domains.yaml:/app/domains.yaml \
           ghcr.io/boveloco/dns-updater:latest
```
