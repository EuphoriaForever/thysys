import sqlite3

conn = sqlite3.connect("thysys.db")

#create a cursor, we use this to do a lotta things
c = conn.cursor()

#create table BUT i commented it out since naa na daan

# c.execute("""CREATE TABLE accounts (
#         account_id INTEGER PRIMARY KEY,
#         account_name text NOT NULL,
#         password text NOT NULL,
#         is_active INTEGER NOT NULL,
#         created_at text NOT NULL,
#         updated_at text ,
#         is_admin INTEGER
#     )""")

#insert pero ako gicomment

# c.execute("INSERT INTO accounts(account_name,password,is_active,created_at,updated_at,is_admin) VALUES ('theeIsmaKwen',"
#           "'12345678010',1,datetime('now','localtime'),NULL,1)")

c.execute("SELECT * FROM accounts")
print(c.fetchall())

# c.execute("DELETE FROM accounts WHERE account_id = 3")

print("Command executed successfully")
#commit our command
conn.commit()

#close our connection
conn.close()