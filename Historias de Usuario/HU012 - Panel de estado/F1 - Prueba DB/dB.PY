import sqlite3

connection = sqlite3.connect('ejemplo.db')
cursor = connection.cursor()

cmd = """CREATE TABLE IF NOT EXISTS Gente(
         first TEXT NOT NULL,
         last TEXT NOT NULL,
         email TEXT NOT NULL PRIMARY KEY,
         birth DATE
     )"""
cursor.execute(cmd)

personas = [('Juan I.', 'Casareski', 'juani.casareski@gmail.com', '17-10-2002'),
            ('Martin N.', 'Casareski', 'martin.casareski@gmail.com', '28-2-2008')]

for first, last, email, birth in personas:
    
    cmd = f"""INSERT INTO Gente (first, last, email, birth) VALUES ('{first}', '{last}', '{email}', '{birth}')"""
    cursor.execute(cmd)
    connection.commit()

