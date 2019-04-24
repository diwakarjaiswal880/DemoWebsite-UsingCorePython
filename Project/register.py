#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "Register Here"
print """
<html>
<head>
</head>
<body>
<center>
<h1>Registration Demo</h1>
<form action="code.py" method="post">
Name
<input type="text" name="name"/>
<br/>
<br/>
F'Name
<input type="text" name="fname"/>
<br/>
<br/>
Gender
<input type="radio" name="a" value="male"/>Male
<input type="radio" name="a" value="female"/>Female
<br/>
<br/>
Email
<input type="email" name="email"/>
<br/>
<br/>
Password
<input type="password" name="password"/>
<br/>
<br/>
<input type="submit" value="Register"/>
</form>
</center>
</body>
</html>


"""