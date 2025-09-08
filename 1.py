from bs4 import BeautifulSoup
import requests
html=requests.get("https://wwww.example.com").text
soup=BeautifulSoup(html,'html5lib')