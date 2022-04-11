print("Content-Type: text/html")
print()
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    #description = description.replace('<', '&lt;')
    #description = description.replace('<', '&gt;')
    title = sanitizer.sanitize(description)

    description = sanitizer.sanitize(description)

    update_link = '<a href="update.py?id={}">uptate</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
           <input type="hidden" name="pageId" value="{}">
           <input type="submit" value="delete">
        </form>
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
print('''<!doctype html>
<html>
<head>
  <title> WEB1 - Welcome</title>
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
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
'''.format(
     title=title,
     desc=description,
     listStr=view.getList(),
     form_default_title=pageID,
     form_default_description=description))
