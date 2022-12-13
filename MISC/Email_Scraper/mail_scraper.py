import requests
from bs4 import BeautifulSoup

url ="https://aftenbladet.no"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
emails = []


for link in soup.find_all("a"):
    email = link.get("href")
    if email and email.startswith("mailto:"):
        email = email[7:] # Remove the "mailto:" part from the email address
        emails.append(email)

print(*emails, sep= "\n")
