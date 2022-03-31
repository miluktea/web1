print("Content-Type: text/html")
print()
import cgi, os

files = os. listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id{name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
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
  <form action="process_creat.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
    <p></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr)
