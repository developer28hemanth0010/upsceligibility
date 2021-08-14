import sqlite3
conn= sqlite3.connect('emails.db')
c= conn.cursor()
# c.execute("""CREATE TABLE email_list (
#         exam text,
#         email text
#         )""")

# c.execute("""INSERT INTO email_list VALUES('test1exam', 'test1email')
#         """)

# c.execute("""DELETE FROM email_list WHERE email = 'vallah@gmail.com'
#         """)
conn.commit()
