import requests
from bs4 import BeautifulSoup
websites = []
emails = []

def link_scanner(url, websites):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
  
    for link in links:
        if link.has_attr('href'):
            if link['href'].startswith('http'):
                websites.append(link['href'])
            else:
                pass
    find_mails(websites)


def find_mails(websites):
    for url in websites:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all("a"):
            email = link.get("href")
            if email and email.startswith("mailto:"):
                email = email[7:]
                if email in emails:
                    pass
                elif "@" in email:  
                    emails.append(email)
                    print(email)
                else:
                    pass

    print(*emails, sep="\n")


link_scanner('https://www.aftenbladet.no', websites)

# to do
# now it finds websites on in the html of specified url and scan those for emails but to find more emails we can scan those websites again for more and more websites instead of stopping on the first ones and scan emails