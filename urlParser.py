# import urllib.request
# import re

# url = "https://en.wikipedia.org/wiki/Neurodiversity"

# def theParser():
#   #url = input('Enter - ')
#   html = urllib.request.urlopen(url).read()
#   print (html)
  #links = re.findall(b'href="(http://.*?)"', html)
  #print (links)
  #for link in links:
  #    print(link.decode())


  # data = urlopen("https://sidlabs.net/")# read only 20 000 chars
  # data = data.split("\n") # then split it into lines
  
  # for line in data:
  #     print (line)

import urllib.request 
from urllib.request import Request
from bs4 import BeautifulSoup
import counter

def theParser():
  url = input('Enter the website to parse -> ') 
  req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
  html = urllib.request.urlopen(req).read()
  
  soup = BeautifulSoup(html, 'html.parser')

  data = soup.get_text().strip()


  #print (soup.find_all('p'))
  #tags = soup.find_all('h1')
  # for tag in tags:
  #    # Look at the parts of a tag
  #    print('TAG:', tag)
  #    print('URL:', tag.get('href', None))
  #    print('Contents:', tag.contents[0])
  #    print('Attrs:', tag.attrs)

  myText = open(r'dataFromWebsite.txt','w')

  for i in data:
      myText.write(i)

  myText.close()
  #print("Writing done!")

  
  counter.letsCount("dataFromWebsite.txt")
  