import mysql.connector as mc
# connect to database
conn = mc.connect(host='localhost', user='root', password='nina9898', db='')
c = conn.cursor()


def showdb():
    c.execute('SHOW DATABASES')
    db = c.fetchall()
    print(db)


def dropmen():
    c.execute('DROP DATABASE IF EXISTS menagerie')


def createmen():
    c.execute('CREATE DATABASE menagerie')


def usemen():
    c.execute('USE menagerie')


def describepet():
    c.execute('USE menagerie')
    c.execute('DESCRIBE pet')
    tb = c.fetchall()
    print(f'{tb}')


def showpet():
    c.execute('USE menagerie')
    c.execute('SELECT * FROM pet')
    sp = c.fetchall()
    print(sp)


def femaledog():
    c.execute('USE menagerie')
    c.execute('SELECT * FROM pet WHERE species = "dog" AND sex = "f"')
    fd = c.fetchall()
    print(fd)


def namebirth():
    c.execute('USE menagerie')
    c.execute('SELECT name,birth FROM pet')
    nb = c.fetchall()
    print(nb)


def numpets():
    c.execute('USE menagerie')
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    np = c.fetchall()
    print(np)


def monthnum():
    c.execute('USE menagerie')
    c.execute('SELECT name,birth,MONTH(birth) FROM pet')
    mn = c.fetchall()
    print(mn)


if __name__ == '__main__':
    monthnum()

