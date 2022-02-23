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
from bs4 import BeautifulSoup


def theParser():
  url = input('Enter the website to parse -> ') 
  html = urllib.request.urlopen(url).read()
  
  soup = BeautifulSoup(html, 'html.parser')
  
  #print (soup.find_all('p'))
  tags = soup.find_all('h1')
  # for tag in tags:
  #    # Look at the parts of a tag
  #    print('TAG:', tag)
  #    print('URL:', tag.get('href', None))
  #    print('Contents:', tag.contents[0])
  #    print('Attrs:', tag.attrs)

  myText = open(r'dataFromWebsite.txt','w')
  
  for tag in tags:
    myList = tag.contents[0]

  for i in myList:
      myText.write(i)

  myText.close()