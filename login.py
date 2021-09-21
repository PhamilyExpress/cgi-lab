#!/usr/bin/env python3
import  cgi, secret
from templates import login_page, secret_page

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

print("Content-Type: text/html;")
if username == secret.username and password == secret.password:
  print("Set-Cookie:UserID = %s;" % username)
  print("Set-Cookie:Password = %s;" % password)

if not username and not password:
  print(login_page())
elif username == secret.username and password == secret.password:
  print(secret_page(username, password))
else:
  print(login_page())
  print("Incorrect credentials")
