from bs4 import BeautifulSoup

soup = BeautifulSoup(open('book.xml'))
'''
print(soup.prettify())  #排版
print(soup.title.name)
print(type(soup.title))
'''
# string
print(soup.title.string)

for item in soup.body.contents:
    print(item)

# CSS查询
a_s = soup.select('book > price')
print()
