from xml.dom import minidom

doc = minidom.parse('book.xml')
root = doc.documentElement
print(type(root))
#print(dir(root))
print(root.nodeName)
books = root.getElementsByTagName('book')
for book in books:
    titles = book.getElementsByTagName('title')
    prices = book.getElementsByTagName('price')
    title = titles[0].childNodes[0].nodeValue
    price = prices[0].childNodes[0].nodeValue
    print(title, price)