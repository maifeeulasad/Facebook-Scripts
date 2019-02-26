import requests
from lxml import html
from bs4 import BeautifulSoup
from PIL import Image
import urllib


count = 0




link ='https://www.facebook.com/photo.php?fbid=1711023345672351&set=a.179171022190932&type=3&theater'



r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")

for t in soup.findAll('img'):
    try:
        t1 =str(t)
        urlD=t['src']
        print(urlD)
        img = Image.open(requests.get(urlD, stream = True).raw)
        name =str(count)+'.jpg'
        img.save(name)
        count +=1
    except:
        pass
    


'''
for t in soup.findAll('img'):
    t1 =str(t)
    if "scaledImageFitWidth img" in t1:
        urlD=t['src']
        print(urlD)
        img = Image.open(requests.get(urlD, stream = True).raw)
        name =str(count)+'.jpg'
        img.save(name)
        count +=1

'''
