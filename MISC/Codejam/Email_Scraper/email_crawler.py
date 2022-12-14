import requests
from bs4 import BeautifulSoup
import os

websites, emails = [], []
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
url = "https://www.vg.no"


def url_scanner():
    html = requests.get(url, headers).text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    websites.append(url)
    for link in links:
        if link.has_attr('href'):
            href = link['href']
            if href.startswith('http'):
                websites.append(href)
                print(href)
            else: pass
    find_mails()


def find_mails():
    os.system("cls")
    for url in websites:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all("a"):
            email = link.get("href")
            if email and email.startswith("mailto:"):
                email = email[7:].strip()
                if email in emails:
                    pass
                elif "@" in email:
                    if "?" in email:
                        email = email[:email.find("?")]
                    elif "=" in email:
                        email = email[:email.find("=")]
                    emails.append(email)
                    print(email)
                else:
                    pass

url_scanner()