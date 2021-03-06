import string
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        self.name = name
        print('element: %s, attrs: %s') % (name, attrs)
    def end_element(self, name):
        print('end element: %s' % name)
    def char_data(self, text):
        if text.strip():
            print("'%s' s text is %s" % (self.name, text))


handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElemnetHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
with open('book.xml', 'r') as f:
    parser.Parse(f.read())
