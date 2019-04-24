#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import cgi
import MySQLdb

data=cgi.FieldStorage()
email=data.getvalue('email')
#print email
password=data.getvalue('password')
#print password

con=MySQLdb.connect("127.0.0.1","root","","knit",3306)
query="select * from register where email='"+email+"' and password='"+password+"'"

cur=con.cursor()

a=cur.execute(query)
con.commit()
con.close()
if a==1:
 print """
 <script>
 
 window.location.href='profile.py'
 </script>
 """
else:
 print """
 <script>
 
 window.location.href='login.py'
 </script>
 """







