#!/usr/bin/env python3
import  cgi, os, requests, secret
from templates import login_page, secret_page

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

print("Content-Type: text/html;")
if username == secret.username and password == secret.password:
  print("Set-Cookie:Username = %s;" % username)
  print("Set-Cookie:Password = %s;" % password)

request = requests.get('http://localhost:8080/login.py')
usernameCookie = request.cookies('Username')
passwordCookie = request.cookies('Password')

if not username and not password:
  print(login_page())
elif usernameCookie == secret.username and passwordCookie == secret.password:
  print(secret_page(username, password))
else:
  print(login_page())
  print("Incorrect credentials")
