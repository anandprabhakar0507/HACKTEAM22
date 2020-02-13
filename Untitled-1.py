import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pycoders",
  passwd="pycoders",
  database="mydatabase"
)
mycursor = mydb.cursor()


#tables creation
mycursor.execute('CREATE TABLE SUBJECTS(subject varchar(255))')

mycursor.execute('CREATE TABLE BIOLOGY(couses varchar(255), grades int , interest varchar(255))')
mycursor.execute('CREATE TABLE MATHS(couses varchar(255), grades int , interest varchar(255))')
mycursor.execute('CREATE TABLE COMMERCE(couses varchar(255), grades int , interest varchar(255))')
mycursor.execute('CREATE TABLE HUMANITIES(couses varchar(255), grades int , interest varchar(255))')

mycursor.execute('CREATE TABLE QUALITIES(course varchar(255), branch varchar(255), understanding int, intelligence int ,sincerity int, thoughfulness int, imagination int, competence int, inquisitive int')

mycursor.execute('CREATE TABLE VALUES(course varchar(255), rating int' )

#mycursor.execute('CREATE TABLE INTERESTS(understanding int, intelligent int ,sincere int, thoughful int, imaginative int, competent int, inquisite int, confidence int')





#core subject table
sql = "INSERT INTO SUBJECT (subject) VALUES (%s, %s)"
val = [
  ('biology'),('maths'),('commerce'),('humanities')
]

mycursor.executemany(sql, val)
mydb.commit()


#biology table
sql = "INSERT INTO BIOLOGY (course , grades , interest) VALUES (%s, %d, %s)"
val = [
  ('MBBS',8),
  ('BAMS',7),
  ('BHMS',7),
  ('BUMS',7),
  ('BDS',6),
  ('Physiotherapy',6),
  ('Nursing',5),
  ('B.Sc',5)
]
mycursor.executemany(sql, val)
mydb.commit()


#maths table
sql = "INSERT INTO MATHS (course , grades, interest) VALUES (%s, %d, %s)"
val = [
  ('B.Tech',7),    
  ('B.Arch',6),
  ('Merchant Navy',7)
  ('BCA',6),
  ('Forensic Science',6)
  ('B.Des',6),
  ('Education and Training',5),
  ('B.Sc',5)
]
mycursor.executemany(sql, val)
mydb.commit()


#commerce table
sql = "INSERT INTO COMMERCE (course , grades, interest) VALUES (%s, %d, %s)"
val = [
  ('CA',8),
  ('CS',7),
  ('CMA',7),
  ('Bachelor in Economics',7),
  ('BBA',7),
  ('BMS',6),
  ('BCA',6),
  ('B.Comm',5)
]
mycursor.executemany(sql, val)
mydb.commit()


#humanities table
sql = "INSERT INTO HUMANITIES (course, grades , interest) VALUES (%s, %d, %s)"
val = [
  ('Sociology',6),
  ('Psychology',6),
  ('Mass Communication',5),
  ('Business and Law',6),
  ('Fashion Designing',5),
  ('Hotel Management',4),
  ('Tourism',4),
  ('BA',4)
]
mycursor.executemany(sql, val)
mydb.commit()


#qualities
sql = "INSERT INTO qualities (course, branch,understanding, intelligence, Sincerity, thoughtfulness,imagination,competence,inquisitive) VALUES (%s,%s,%d,%d,%d,%d,%d,%d,%d)"

val = [('MBBS','bio',4,4,5,2,2,5,4),
  ('BAMS','bio',4,4,4,1,2,4,3),
  ('BHMS','bio',4,4,3,2,1,3,3),
  ('BUMS','bio',3,3,3,4,2,5,2),
  ('BDS','bio',5,3,4,3,2,1,4),
  ('Physiotherapy','bio',5,5,1,1,1,2,3),
  ('Nursing','bio',5,2,2,2,3,3,2),
  ('B.Sc','bio',4,3,3,2,1,4,4),

  ('B.Tech','maths',7),    
  ('B.Arch','maths',6),
  ('Merchant Navy','maths',7)
  ('BCA','maths',6),
  ('Forensic Science','maths',6)
  ('B.Des','maths',6),
  ('Education and Training','maths',5),
  ('B.Sc','maths',5),

  ('CA','commerce',8),
  ('CS','commerce',7),
  ('CMA','commerce',7),
  ('Bachelor in Economics','commerce',7),
  ('BBA','commerce',7),
  ('BMS','commerce',6),
  ('BCA','commerce',6),
  ('B.Comm','commerce',5),
              
  ('Sociology','humanities',6),
  ('Psychology','humanities',6),
  ('Mass Communication','humanities',5),
  ('Business and Law','humanities',6),
  ('Fashion Designing','humanities',5),
  ('Hotel Management','humanities',4),
  ('Tourism','humanities',4),
  ('BA','humanities',4)
       
       
##frontend gui



#sub is the core subject that the user had in 12th class
#marks and curiosity is entered by the user on the frontend

mycursor.execute("SELECT course FROM (SELECT subject FROM SUBJECTS WHERE subject = sub) WHERE grades < marks")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)