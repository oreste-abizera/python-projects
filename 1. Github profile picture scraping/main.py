import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github user: ")
r = requests.get("https://github.com/"+github_user)