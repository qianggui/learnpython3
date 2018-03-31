#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<1-->', data, '-->')

    def handle_entityref(self, name):
        print('&%s' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
    <!-- test html parser -->
    <p>
        some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END
    </p>
</body>
</html>''')