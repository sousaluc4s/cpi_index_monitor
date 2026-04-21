# core/downloader.py
import os
import requests

def download(url, folder="CPI"):
    os.makedirs(folder, exist_ok=True)

    filename = url.split("/")[-1]
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        print(f"Already exists: {filename}")
        return path

    response = requests.get(url)
    response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)

    print(f"Downloaded: {filename}")
    return path