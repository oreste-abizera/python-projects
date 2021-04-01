import requests
from bs4 import BeautifulSoup as bs

githubUser = input("Input Github user: ")
r = requests.get("https://github.com/"+githubUser)

soup = bs(r.content, "html.parser")
profileImageUrl = soup.find("img", { "alt" : "Avatar" })["src"]
print(profileImageUrl)