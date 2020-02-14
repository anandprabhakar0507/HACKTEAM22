import mysql.connector

mydb = mysql.connector.connect(
  host ='localhost',
  user ='pycoders',
  passwd ='pycoders',
  database ='mydatabase'
)
mycursor = mydb.cursor()


#tables creation
mycursor.execute('CREATE TABLE SUBJECTS(subject varchar(255))')

mycursor.execute('CREATE TABLE BIOLOGY(couses varchar(255), grades int , interest varchar(255))')
mycursor.execute('CREATE TABLE MATHS(couses varchar(255), grades int , interest varchar(255))')
mycursor.execute('CREATE TABLE COMMERCE(couses varchar(255), grades int , interest varchar(255))')
mycursor.execute('CREATE TABLE HUMANITIES(couses varchar(255), grades int , interest varchar(255))')

mycursor.execute('CREATE TABLE QUALITIES(course varchar(255), branch varchar(255), understanding int, intelligence int ,sincerity int, thoughfulness int, imagination int, competence int, inquisitive int')

mycursor.execute('CREATE TABLE VALUES(course varchar(255), rating int')

mycursor.execute('CREATE TABLE DETAILS(NAME VARCHAR(255),SEX VARCHAR(255),EMAILID VARCHAR(255), DOB VARCHAR(255))')



#core subject table
sql = "INSERT INTO SUBJECT (subject) VALUES (%s, %s)"
val = [
  ("biology"),("maths"),("commerce"),("humanities")
]

mycursor.executemany(sql, val)
mydb.commit()


#biology table
sql = "INSERT INTO BIOLOGY (course , grades) VALUES (%s, %d)"
val = [
  ("MBBS",8),
  ("BAMS",7),
  ("BHMS",7),
  ("BUMS",7),
  ("BDS",6),
  ("Physiotherapy",6),
  ("Nursing",5),
  ("B.Sc",5)
]
mycursor.executemany(sql, val)
mydb.commit()


#maths table
sql = "INSERT INTO MATHS (course , grades) VALUES (%s, %d)"
val = [
  ("B.Tech",7),    
  ("B.Arch",6),
  ("Merchant Navy",7)
  ("BCA",6),
  ("Forensic Science",6)
  ("B.Des",6),
  ("Education and Training",5),
  ("B.Sc",5)
]
mycursor.executemany(sql, val)
mydb.commit()


#commerce table
sql = "INSERT INTO COMMERCE (course , grades) VALUES (%s, %d)"
val = [
  ("CA",8),
  ("CS",7),
  ("CMA",7),
  ("Bachelor in Economics",7),
  ("BBA",7),
  ("BMS",6),
  ("BCA",6),
  ("B.Comm",5)
]
mycursor.executemany(sql, val)
mydb.commit()


#humanities table
sql = "INSERT INTO HUMANITIES (course, grades) VALUES (%s, %d)"
val = [
  ("Sociology",6),
  ("Psychology",6),
  ("Mass Communication",5),
  ("Business and Law",6),
  ("Fashion Designing",5),
  ("Hotel Management",4),
  ("Tourism",4),
  ("BA",4)
]
mycursor.executemany(sql, val)
mydb.commit()


#qualities
sql = "INSERT INTO qualities (course, branch,understanding, intelligence, Sincerity, thoughtfulness,imagination,competence,inquisitive) VALUES (%s,%s,%d,%d,%d,%d,%d,%d,%d)"

val = [("MBBS","bio",4,4,5,2,2,5,4),
  ("BAMS","bio",4,4,4,1,2,4,3),
  ("BHMS","bio",4,4,3,2,1,3,3),
  ("BUMS","bio",3,3,3,4,2,5,2),
  ("BDS","bio",5,3,4,3,2,1,4),
  ("Physiotherapy","bio",5,5,1,1,1,2,3),
  ("Nursing","bio",5,2,2,2,3,3,2),
  ("B.Sc","bio",4,3,3,2,1,4,4),

  ("B.Tech","maths",4,4,5,2,2,5,4),    
  ("B.Arch","maths",4,4,4,1,2,4,3),
  ("Merchant Navy","maths",4,4,3,2,1,3,3)
  ("BCA","maths",3,3,3,4,2,5,2),
  ("Forensic Science","maths",5,3,4,3,2,1,4)
  ("B.Des","maths",5,5,1,1,1,2,3),
  ("Education and Training","maths",5,2,2,2,3,3,2),
  ("B.Sc","maths",4,3,3,2,1,4,4),

  ("CA","commerce",4,4,5,2,2,5,4),
  ("CS","commerce",4,4,4,1,2,4,3),
  ("CMA","commerce",4,4,3,2,1,3,3),
  ("Bachelor in Economics","commerce",3,3,3,4,2,5,2),
  ("BBA","commerce",5,3,4,3,2,1,4),
  ("BMS","commerce",5,5,1,1,1,2,3),
  ("BCA","commerce",5,2,2,2,3,3,2),
  ("B.Comm","commerce",4,3,3,2,1,4,4),
              
  ("Sociology","humanities",4,4,5,2,2,5,4),
  ("Psychology","humanities",4,4,4,1,2,4,3),
  ("Mass Communication","humanities",4,4,3,2,1,3,3),
  ("Business and Law","humanities",3,3,3,4,2,5,2),
  ("Fashion Designing","humanities",5,3,4,3,2,1,4),
  ("Hotel Management","humanities",5,5,1,1,1,2,3),
  ("Tourism","humanities",5,2,2,2,3,3,2),
  ("BA","humanities",4,3,3,2,1,4,4)
]
       

##frontend gui



#sub is the core subject that the user had in 12th class
#marks and curiosity is entered by the user on the frontend


#recommendation system
sub = mycursor.execute("SELECT branch FROM DETAILS")
marks = mycursor.execute("SELECT marks FROM DETAILS")

table = mycursor.execute("SELECT course FROM (SELECT subject FROM SUBJECTS WHERE subject = sub) where grade < marks")

qualities_table = mycursor.execute("SELECT count(understanding, intelligence, Sincerity, thoughtfulness,imagination,competence,inquisitive) FROM table where understanding = '1'and  intelligence = '1' and Sincerity = '1' and thoughtfulness = '1' and imagination='1' and competence='1' and inquisitive='1'")

qualities_user = mycursor.execute("SELECT count(understanding, intelligence, Sincerity, thoughtfulness,imagination,competence,inquisitive) FROM qualityu where understanding = '1'and  intelligence = '1' and Sincerity = '1' and thoughtfulness = '1' and imagination='1' and competence='1' and inquisitive='1'")

final_table = if(qualities_table<=qualities_user)["select course from table":NULL]
mycursor.execute("SELECT course FROM final_table")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)