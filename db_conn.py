import sqlite3

#connect to db
conn= sqlite3.connect('dates.db')


#create a cursor
c= conn.cursor()

# c.execute("""CREATE TABLE afcat_fb (
#         sno text,
#         course text,
#         starting_date date,
#         ending_date date )""")

# many_nda= [
#         
#         ]


# c.executemany("INSERT INTO nda VALUES (?,?,?,?)", (many_nda))

# many_cds_ima_ina=[
    
# ]

# c.execute("""CREATE TABLE cds_afa (
#         sno text,
#         course text,
#         starting_date date,
#         ending_date date )""")

# many_cds_afa=[
        
# ]

# c.execute("""CREATE TABLE cds_ota_men_women (
#         sno text,
#         course text,
#         starting_date date,
#         ending_date date )""")

# many_afcat_fb=[

# ]

# c.executemany("INSERT INTO afcat_fb VALUES (?,?,?,?)", (many_afcat_fb))
# c.execute("""DROP TABLE cds_ota_men_women;""")
conn.commit()
