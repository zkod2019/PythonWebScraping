import requests
from bs4 import BeautifulSoup

def google():
    result = requests.get("https://www.google.com/")

    print(result.status_code) #200 for OK
    print(result.headers) #for HTTP header
    src = result.content #storing source of page in variable
    # print(src)

    soup = BeautifulSoup(src, 'lxml') #creating a soup obj
    links = soup.find_all("a") #find all links (cuz <a> tag)
    print("\n")
    print(links)
    print("\n")

    for link in links: #find specific lin
        if "Gmail" in link.text: #if "about" is the text from link
            print(link)
            print(link.attrs['href'])

def another():
    

if __name__ == "__main__":
    option = input("Website you want to scrape:"\
    "\n1. Google"\
    "\n2. Another")

    print("Option is:" + option)
    if (option == "1"):
        google()
    