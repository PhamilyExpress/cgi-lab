#!/usr/bin/env python3
import  cgi, os, secret, http.cookies
from templates import login_page, secret_page

form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

print("Content-Type: text/html;")
if username == secret.username and password == secret.password:
  print("Set-Cookie:Username = %s;" % username)
  print("Set-Cookie:Password = %s;" % password)

cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])

usernameCookie = ""
passwordCookie = ""

if cookie.get("Username") and cookie.get("Password"):
  usernameCookie = cookie.get("Username").value
  passwordCookie = cookie.get("Password").value

if username == None or password == None:
  print(login_page())
elif usernameCookie == secret.username and passwordCookie == secret.password:
  print(secret_page(username, password))
else:
  print(login_page())
  print("Incorrect credentials")
