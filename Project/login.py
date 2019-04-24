#!C:\python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>Login Page</title>
</head>
<body>
<center>
<h1>Login Here</h1>
<form action="logcode.py" method="post">
Email<input type="email" name="email"/>
<br/>
<br/>
Password
<input type="password" name="password"/>
<br/><br/>
<input type="submit" value="Login"/>
</form>
<a href="register.py">New Registeration</a>
</center>
</body>
</html>
"""