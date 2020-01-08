# Challenge: At the moment, our Head class doesn't create header with anything in it.
# So your challenge is to modify the program so that the Head class can include a Title tag.
# Your HTML should look something like this:
# <head>
#   <title>Document Title</title>
# </head>
# Text for the title will be passed to the HtmlDoc class init method when the document's
# created.


class Tag(object):
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents
    
    def __str__(self):
        return("{0.start_tag}{0.contents}{0.end_tag}".format(self))

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"', '')
        self.end_tag = '' # DOCTYPE doesn't have and end tag


class Head(Tag):
    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):
    def __init__(self):
        super().__init__('body', '') # body content will be built up separately
        self.body_contents = []
    
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.body_contents.append(new_tag)
    
    def display(self, file=None):
        for tag in self.body_contents:
            self.contents += str(tag)
        
        super().display(file=file)

class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body
    
    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)
    
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)

if __name__ == '__main__':
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                        " of objects to build up another obkect.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
                        " - if it's destroyed, those objects continue to exist.")
    new_docType = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_docType, new_header, new_body)

    with open('game/test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)
