import sqlite3

#connect to db
conn= sqlite3.connect('/Users/hemanthdatta/Codess/dates.db')


#create a cursor
c= conn.cursor()

# c.execute("""CREATE TABLE cds_ima_ina (
#         sno text,
#         course text,
#         starting_date date,
#         ending_date date )""")

# many_nda= [
#         ('1', 'NDA 140', '1999-01-02', '2002-01-01'),
#         ('2', 'NDA 141', '1999-07-02', '2002-07-01'),
#         ('3', 'NDA 142', '2000-02-01', '2003-01-01'),
#         ('4', 'NDA 143', '2000-02-07', '2003-01-07'),
#         ('5', 'NDA 144', '2001-02-01', '2004-01-01'),
#         ('6', 'NDA 145', '2001-02-07', '2004-01-07'),
#         ('7', 'NDA 146', '2002-02-01', '2005-01-01'),
#         ('8', 'NDA 147', '2002-02-07', '2005-01-07'),
#         ('9', 'NDA 148', '2003-02-01', '2006-01-01'),
#         ('10', 'NDA 149', '2003-02-07', '2006-01-07'),
#         ('11', 'NDA 150', '2004-02-01', '2007-01-01'),
#         ('12', 'NDA 151', '2004-02-07', '2007-01-07'),
#         ('13', 'NDA 152', '2005-02-01', '2008-01-01'),
#         ('14', 'NDA 153', '2005-02-07', '2008-01-07'),
#         ('15', 'NDA 154', '2006-02-01', '2009-01-01'),
#         ('16', 'NDA 155', '2006-02-07', '2009-01-07'),
#         ('17', 'NDA 156', '2007-02-01', '2010-01-01'),
#         ('18', 'NDA 157', '2007-02-07', '2010-01-07'),
#         ('19', 'NDA 158', '2008-02-01', '2011-01-01'),
#         ('20', 'NDA 159', '2008-02-07', '2011-01-07'),
#         ('21', 'NDA 160', '2009-02-01', '2012-01-01'),
#         ('22', 'NDA 161', '2009-02-07', '2012-01-07'),
#         ('23', 'NDA 162', '2010-02-01', '2013-01-01'),
#         ('24', 'NDA 163', '2010-02-07', '2013-01-07'),
#         ('25', 'NDA 164', '2011-02-01', '2014-01-01'),
#         ('26', 'NDA 165', '2011-02-07', '2014-01-07'),
#         ('27', 'NDA 166', '2012-02-01', '2015-01-01'),
#         ('28', 'NDA 167', '2012-02-07', '2015-01-07'),
#         ('29', 'NDA 168', '2013-02-01', '2016-01-01'),
#         ('30', 'NDA 169', '2014-02-07', '2016-01-07'),
#         ]


# c.executemany("INSERT INTO nda VALUES (?,?,?,?)", (many_nda))

# many_cds_ima_ina=[
#         ('1', 'CDS 1 2017', '1994-01-02', '1999-01-01'),
#         ('2', 'CDS 2 2017', '1994-07-02', '1999-07-01'),
#         ('3', 'CDS 1 2018', '1995-01-02', '2000-01-01'),
#         ('4', 'CDS 2 2018', '1995-07-02', '2000-07-01'),
#         ('5', 'CDS 1 2019', '1996-01-02', '2001-01-01'),
#         ('6', 'CDS 2 2019', '1996-07-02', '2001-07-01'),
#         ('7', 'CDS 1 2020', '1997-01-02', '2002-01-01'),
#         ('8', 'CDS 2 2020', '1997-07-02', '2002-07-01'),
#         ('9', 'CDS 1 2021', '1998-01-02', '2003-01-01'),
#         ('10', 'CDS 2 2021', '1998-07-02', '2003-07-01'),
#         ('11', 'CDS 1 2022', '1999-01-02', '2004-01-01'),
#         ('12', 'CDS 2 2022', '1999-07-02', '2004-07-01'),
#         ('13', 'CDS 1 2023', '2000-01-02', '2005-01-01'),
#         ('14', 'CDS 2 2023', '2000-07-02', '2005-07-01'),
#         ('15', 'CDS 1 2024', '2001-01-02', '2006-01-01'),
#         ('16', 'CDS 2 2024', '2001-07-02', '2006-07-01'),
#         ('17', 'CDS 1 2025', '2002-01-02', '2007-01-01'),
#         ('18', 'CDS 2 2025', '2002-07-02', '2007-07-01'),
#         ('19', 'CDS 1 2026', '2003-01-02', '2008-01-01'),
#         ('20', 'CDS 2 2026', '2003-07-02', '2008-07-01'),
#         ('21', 'CDS 1 2027', '2004-01-02', '2009-01-01'),
#         ('22', 'CDS 2 2027', '2004-07-02', '2009-07-01'),
#         ('23', 'CDS 1 2028', '2005-01-02', '2010-01-01'),
#         ('24', 'CDS 2 2028', '2005-07-02', '2010-07-01'),
#         ('25', 'CDS 1 2029', '2006-01-02', '2011-01-01'),
#         ('26', 'CDS 2 2029', '2006-07-02', '2011-07-01'),
#         ('27', 'CDS 1 2030', '2007-01-02', '2012-01-01'),
#         ('28', 'CDS 2 2030', '2007-07-02', '2012-07-01'),
#         ('29', 'CDS 1 2031', '2008-01-02', '2013-01-01'),
#         ('30', 'CDS 2 2031', '2008-07-02', '2013-07-01'),
# ]

# c.execute("""CREATE TABLE cds_afa (
#         sno text,
#         course text,
#         starting_date date,
#         ending_date date )""")

# many_cds_afa=[
#             ('1', 'CDS 1 2017', '1994-01-02', '1998-01-01'),
#             ('2', 'CDS 2 2017', '1994-07-02', '1998-07-01'),
#             ('3', 'CDS 1 2018', '1995-01-02', '1999-01-01'),
#             ('4', 'CDS 2 2018', '1995-07-02', '1999-07-01'),
#             ('5', 'CDS 1 2019', '1996-01-02', '2000-01-01'),
#             ('6', 'CDS 2 2019', '1996-07-02', '2000-07-01'),
#             ('7', 'CDS 1 2020', '1997-01-02', '2001-01-01'),
#             ('8', 'CDS 2 2020', '1997-07-02', '2001-07-01'),
#             ('9', 'CDS 1 2021', '1998-01-02', '2002-01-01'),
#             ('10', 'CDS 2 2021', '1998-07-02', '2002-07-01'),
#             ('11', 'CDS 1 2022', '1999-01-02', '2003-01-01'),
#             ('12', 'CDS 2 2022', '1999-07-02', '2003-07-01'),
#             ('13', 'CDS 1 2023', '2000-01-02', '2004-01-01'),
#             ('14', 'CDS 2 2023', '2000-07-02', '2004-07-01'),
#             ('15', 'CDS 1 2024', '2001-01-02', '2005-01-01'),
#             ('16', 'CDS 2 2024', '2001-07-02', '2005-07-01'),
#             ('17', 'CDS 1 2025', '2002-01-02', '2006-01-01'),
#             ('18', 'CDS 2 2025', '2002-07-02', '2006-07-01'),
#             ('19', 'CDS 1 2026', '2003-01-02', '2007-01-01'),
#             ('20', 'CDS 2 2026', '2003-07-02', '2007-07-01'),
#             ('21', 'CDS 1 2027', '2004-01-02', '2008-01-01'),
#             ('22', 'CDS 2 2027', '2004-07-02', '2008-07-01'),
#             ('23', 'CDS 1 2028', '2005-01-02', '2009-01-01'),
#             ('24', 'CDS 2 2028', '2005-07-02', '2009-07-01'),
#             ('25', 'CDS 1 2029', '2006-01-02', '2010-01-01'),
#             ('26', 'CDS 2 2029', '2006-07-02', '2010-07-01'),
#             ('27', 'CDS 1 2030', '2007-01-02', '2011-01-01'),
#             ('28', 'CDS 2 2030', '2007-07-02', '2011-07-01'),
#             ('29', 'CDS 1 2031', '2008-01-02', '2012-01-01'),
#             ('30', 'CDS 2 2031', '2008-07-02', '2012-07-01'),
# ]

# c.execute("""CREATE TABLE cds_ota_men_women (
#         sno text,
#         course text,
#         starting_date date,
#         ending_date date )""")

# many_cds_ota_men_women=[

#                 ('1', 'CDS 1 2017', '1993-01-02', '1999-01-01'),
#                 ('2', 'CDS 2 2017', '1993-07-02', '1999-07-01'),
#                 ('3', 'CDS 1 2018', '1994-01-02', '2000-01-01'),
#                 ('4', 'CDS 2 2018', '1994-07-02', '2000-07-01'),
#                 ('5', 'CDS 1 2019', '1995-01-02', '2001-01-01'),
#                 ('6', 'CDS 2 2019', '1995-07-02', '2001-07-01'),
#                 ('7', 'CDS 1 2020', '1996-01-02', '2002-01-01'),
#                 ('8', 'CDS 2 2020', '1996-07-02', '2002-07-01'),
#                 ('9', 'CDS 1 2021', '1997-01-02', '2003-01-01'),
#                 ('10', 'CDS 2 2021', '1997-07-02', '2003-07-01'),
#                 ('11', 'CDS 1 2022', '1998-01-02', '2004-01-01'),
#                 ('12', 'CDS 2 2022', '1998-07-02', '2004-07-01'),
#                 ('13', 'CDS 1 2023', '1999-01-02', '2005-01-01'),
#                 ('14', 'CDS 2 2023', '1999-07-02', '2005-07-01'),
#                 ('15', 'CDS 1 2024', '2000-01-02', '2006-01-01'),
#                 ('16', 'CDS 2 2024', '2000-07-02', '2006-07-01'),
#                 ('17', 'CDS 1 2025', '2001-01-02', '2007-01-01'),
#                 ('18', 'CDS 2 2025', '2001-07-02', '2007-07-01'),
#                 ('19', 'CDS 1 2026', '2002-01-02', '2008-01-01'),
#                 ('20', 'CDS 2 2026', '2002-07-02', '2008-07-01'),
#                 ('21', 'CDS 1 2027', '2003-01-02', '2009-01-01'),
#                 ('22', 'CDS 2 2027', '2003-07-02', '2009-07-01'),
#                 ('23', 'CDS 1 2028', '2004-01-02', '2010-01-01'),
#                 ('24', 'CDS 2 2028', '2004-07-02', '2010-07-01'),
#                 ('25', 'CDS 1 2029', '2005-01-02', '2011-01-01'),
#                 ('26', 'CDS 2 2029', '2005-07-02', '2011-07-01'),
#                 ('27', 'CDS 1 2030', '2006-01-02', '2012-01-01'),
#                 ('28', 'CDS 2 2030', '2006-07-02', '2012-07-01'),
#                 ('29', 'CDS 1 2031', '2007-01-02', '2013-01-01'),
#                 ('30', 'CDS 2 2031', '2007-07-02', '2013-07-01'),


# ]

# c.executemany("INSERT INTO cds_ota_men_women VALUES (?,?,?,?)", (many_cds_ota_men_women))
conn.commit()