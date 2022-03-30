import cgi, os

files = os. listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id{name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()

'''.format(title=pageId, desc=description, listStr=listStr)
