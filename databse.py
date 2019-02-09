import MySQLdb

class Database:
    host = "localhost"
    user = "test user"
    passwd = "testpass"
    db = "test"

    def __init__(self):
        self.connection = MYsqlDB.connect(host = self.host,
    user = self.user,
    passwd = self.passwd,
    db = self.db)
        
    def query(self,q):
        cursor = self.connection.cursor(Mysqldb.cursor.DictCursor)
        cursor.execute(q)

        return cursor.fetchall()
    def __del__(self):
        self.connection.close()

if __name__ == "__main__":
     db ="DELETE FROM testable"

     db.query(q)

     q = """INSERT INTO TESTTABLE{'NAME','AGE'}VALUES{'MIKE',39},{'MICHAEL',21},{'ANGELA',21}"""

     db.query(q)

     q = """ SELECT * FROM testtable where age = 21"""
     people = db.query(q)

     for person in people:
        print("Found %s " %person['NAME'])
