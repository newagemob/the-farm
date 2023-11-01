import os
import random
import requests
from pathlib import Path
from utils.proxies import scrape_proxies


parent_dir = Path(__file__).parent


test_url = "https://google.com"

# get random proxy from proxies_list.txt


def recycle_proxies():
    if os.path.exists(f"{parent_dir}/proxies_list.txt"):
        os.remove(f"{parent_dir}/proxies_list.txt")

    scrape_proxies()


def check_proxy(proxy):
    print("Checking for a good proxy... This might take some time.")
    try:
        session = requests.Session()
        session.proxies = {'http': proxy, 'https': proxy}
        session.get(test_url, timeout=5)
        print(f"Proxy {proxy} is working")
        return proxy
    except Exception as e:
        # print(f"PASS {proxy} is not working")
        return False


def find_proxy():
    proxies = []
    with open(f"{parent_dir}/proxies_list.txt", "r") as file:
        for line in file:
            proxies.append(line.strip())
    
    for proxy in random.sample(proxies, len(proxies)):
        # wait for a good proxy, then return it
        if check_proxy(proxy):
            return proxy
