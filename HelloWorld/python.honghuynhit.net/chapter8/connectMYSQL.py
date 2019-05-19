import MySQLdb
db = None
try:
    db = MySQLdb.connect(host = 'localhost', user ='root', passwd = 'root', db = 'mysql')
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
if db:
cur = db.cursor()
cur.execute("SELECT VERSION()")
ver = cur.fetchone()
print "Database version : %s " % ver