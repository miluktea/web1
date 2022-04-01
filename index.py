print("Content-Type: text/html")
print()
import cgi, os

files = os. listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id{name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    update_link = '<a href="update.py?id={}">uptate</a>'.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title> WEB1 - Welcome</title>
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="creat.py">create</a>
  <form action="process_update.py" method="post">
       <input type="hidden" name="pageId" value="{form_default_title}">
       <p><input type="text" name="title" placeholder="title" value="{form_defalt_title}"></p>
       <p><textarea rows="4" name="description" placeholder="description">{form_default_desciption}</textarea></p>
       <p><input type="submit"></p>
       <p></p>
   </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, form_default_title=pageID, form_default_description=description))
