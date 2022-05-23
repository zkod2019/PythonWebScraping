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

def bbcNews():
    result = requests.get("https://www.bbc.com/news/science-environment-56837908")
    src = result.content
    soup = BeautifulSoup(src, 'lxml') 
    urls = []

    for divtag in soup.find_all("div"):
        atag = divtag.find('a')
        urls.append(atag.attrs['href'])

    print(urls)
    

if __name__ == "__main__":
    option = input("Website you want to scrape:"\
    "\n1. Google"\
    "\n2. BBC News\n")

    print("Option is:" + option)
    if (option == "1"):
        google()
    if (option == "2"):
        bbcNews()
    