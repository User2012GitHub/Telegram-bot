import sqlite3

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS medicine '
'(id INT, name TEXT, bdate INT, price INT)')

cursor.execute('''INSERT INTO medicine (id, name, bdate, price) 
VALUES (1, 'Paratsetamol', '1 year', '5000')''')
cursor.execute('''INSERT INTO  medicine (id, name, bdate, price)
