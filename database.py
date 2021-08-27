import sqlite3

conn = sqlite3.connect("thysys.db")

#create a cursor, we use this to do a lotta things
c = conn.cursor()

#create table BUT i commented it out since naa na daan

# c.execute("""CREATE TABLE IF NOT EXISTS accounts (
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

# c.execute("SELECT * FROM accounts")
# print(c.fetchall())

# c.execute("DELETE FROM accounts WHERE account_id = 3")

#        values = [age, gender, pregnant, trimester, goitre, smoke, hairloss, constipation, diarrhea, family, nervous,
#                  skin, menstrualBleeding, tired, sleepiness, weight, heart, temp] and class and USERNAME


# c.execute("""CREATE TABLE IF NOT EXISTS results (
#         result_id INTEGER PRIMARY KEY,
#         username text NOT NULL, [1]
#         age text NOT NULL,[2]
#         gender text NOT NULL,
#         pregnant text NOT NULL,[4]
#         trimester text NOT NULL,
#         goitre text NOT NULL,[6]
#         smoke text NOT NULL,
#         hairloss text NOT NULL, [8]
#         constipation text NOT NULL,
#         diarrhea text NOT NULL,
#         family text NOT NULL,[11]
#         nervous text NOT NULL,
#         skin text NOT NULL,  [13]
#         menstrual text NOT NULL,
#         tired text NOT NULL,
#         sleepiness text NOT NULL,
#         weight text NOT NULL, [17]
#         heart text NOT NULL,  [18]
#         temp text NOT NULL, [19]
#         class text NOT NULL,
#         created_at text NOT NULL
#     )""")

c.execute("SELECT * FROM results")
print(c.fetchall())

# c.execute("DROP TABLE results")
# c.execute("DELETE FROM results WHERE result_id = 2")
print("Command executed successfully")
#commit our command
conn.commit()

#close our connection
conn.close()