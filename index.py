#! C:\Program Files\Python310\python.exe
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''<!doctype html>
<html>
<head>
  <title>web1-welcome</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1><a href="index.py?id=WEB">web</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">html</a></li>
    <li><a href="index.py?id=CSS">css</a></li>
    <li><a href="index.py?id=JavaScript">javascript</a></li>
  </ol>
  <h2>{title}</h2>
  <p></p>
</body>
</html>
'''.format(title=pageId))
