import requests
from bs4 import BeautifulSoup

def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return ""

if __name__ == "__main__":
    url = "https://example.com"
    text = fetch_text_from_url(url)
    print(text)
