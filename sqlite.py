import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
CREATE TABLE Student(Name VARCHAR(25),Class VARCHAR(25),
Section VARCHAR(25), Marks INT)
"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO Student VALUES ('Prince', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO Student VALUES ('John', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO Student VALUES ('Mukesh', 'Machine Learning', 'A', 90)''')
cursor.execute('''INSERT INTO Student VALUES ('Jacob', 'Full Stack', 'A', 90)''')
cursor.execute('''INSERT INTO Student VALUES ('Dipesh', 'DEVOPS', 'A', 90)''')

print("The inserted records are:")
data = cursor.execute('''SELECT * FROM Student''')
for row in data:
    print(row)

connection.commit()
connection.close()