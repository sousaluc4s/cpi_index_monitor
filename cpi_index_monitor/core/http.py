# core/http.py
import requests

def get(url, timeout=10):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response