from HTMLParser import HTMLParser

class MyParser(HTMLParser):
    def handle_decl(self, decl):
        HTMLParser.handle_decl(self, decl)
        print('decl %s' % decl)
    def handle_startag(self, tag, attrs):
        HTMLParser.handle_starttag(self, tag, attrs)
        print('<' + tag + '>')
    def handle_endtag(self, tag):
        HTMLParser.handle_endtag(self, tag)
        print('<' + tag + '>')
    def handle_data(self, data):
        HTMLParser.handle_data(self, data)
        print('data %s' % data)
    def handle_startendtag(self, tag, attrs):
        HTMLParser.handel_comment(self, data)

    def close(self):
        HTMLParser.close(self)
        print('close')

demo = MyParser()
demo.feed(open('book.xml').read)
demo.close()
