import sqlite3


def create_db():
    conn = sqlite3.connect('pcw.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS USER_TABLE
             (ID INT PRIMARY KEY,
             FIRSTNAME TEXT NOT NULL,
             LASTNAME TEXT NOT NULL,
             MOBILE INT NOT NULL,
             EMAIL TEXT,
             PASSWORD TEXT);''')
    return conn


def insert_data(firstname, lastname, mobile, email, password):
    conn = create_db()
    conn.execute("INSERT INTO USER_TABLE (ID,FIRSTNAME,LASTNAME,MOBILE,EMAIL,PASSWORD)"
                 " VALUES (NULL, '"+firstname+"', '"+lastname+"', "+mobile+", '"+email+"', '"+password+"' )")
    conn.commit()
    conn.close()
    return 1


def view_data():
    conn = create_db()
    cursor = conn.execute("SELECT id, firstname, lastname, mobile, email, password from USER_TABLE")
    for row in cursor:
        print("ID = ", row[0])
        print("FIRSTNAME = ", row[1])
        print("LASTNAME = ", row[2])
        print("MOBILE = ", row[3])
        print("EMAIL = ", row[4])
        print("PASSWORD = ", row[5])
    conn.close()


def login(email, password):
    conn = create_db()
    cursor = conn.execute("SELECT * from USER_TABLE where email='"+email+"'")

    for row in cursor:
        if password == row[5]:
            return 1
    conn.close()
    return 0

view_data()