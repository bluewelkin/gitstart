import MySQLdb

try:
   connection = MySQLdb.connect(user="root",passwd="admin",host="localhost",db="test")
   print "Could  connect to MySQL server."
except:
   print "Could not connect to MySQL server."
   exit( 0 )

