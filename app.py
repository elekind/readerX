from flask import Flask
import requests
from bs4 import BeautifulSoup
import templates as tmplt

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"}
""" url = "https://www.economist.com/asia/2024/07/11/the-worlds-next-food-superpower"

r = requests.get("https://archive.is/latest/" + url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml').article.div.div """

app = Flask(__name__)

@app.route("/<path:link>")
def clean(link):
    
    return tmplt.clean_up(link, headers)


""" @app.route("<path:link>")
def intro(link):

    return "<p>Hello, World!</p>" 
    
delete whitespace on top. Use | to find and strip.

Use find_all and next. Get images to load.

Use true and delete all style elements

Use local html  """