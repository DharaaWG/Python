import requests
res=requests.get("http://example.com/")
print(type(res))
print(res.text)
import bs4
soup=bs4.BeautifulSoup(res.text,"lxml")
print(soup)
print(soup.select('title'))
print(soup.select('p'))
para=soup.select("p")
print(para[0].getText())
print('\n')
req=requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup=bs4.BeautifulSoup(req.text,"lxml")
#print(soup)
print(soup.select('.toctext'))
for item in soup.select('.toctext'):
    print(item.text)

print('\n')
req1=requests.get("https://en.wikipedia.org/wiki/Wikipedia:Ten_things_you_may_not_know_about_images_on_Wikipedia")
soup=bs4.BeautifulSoup(req1.text,"lxml")
print(soup.select('img')[0])
ifo=soup.select('.thumbimage')
print(ifo)
comp=ifo[0]
print('\n\n')
print(comp['src'])
#<img src="https://upload.wikimedia.org/wikipedia/commons/a/a3/%22Wind_Mountain%22_Columbia_R_-_NARA_-_102278851_%28page_1%29.png">
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
print(image_link.content)
print('\n\n')
f=open('comp.jpg','wb')
print(f.write(image_link.content))
f.close()

print('\n\n')
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
res = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(res.text,"lxml")
soup.select(".product_pod")
products = soup.select(".product_pod")
example = products[0]
print(type(example))
two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])
print(two_star_titles)





