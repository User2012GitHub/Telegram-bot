import sqlite3

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS medicine '
'(id INT, name TEXT, bdate INT, price INT)')

cursor.execute('''INSERT INTO medicine (id, name, bdate, price) 
VALUES (1, 'Paratsetamol', '1 year', '5000')''')
cursor.execute('''INSERT INTO  medicine (id, name, bdate, price)
VALUES (5, 'Anzibel', '8 months', '12000')''')
cursor.execute('''INSERT INTO  medicine (id, name, bdate, price)
VALUES (3, 'Trimol', '7 months', '26000')''')

conn.commit()

def goodbye():
    pass

cursor.execute('''SELECT * FROM medicine''')
about = input("Dori nomini kiriting: ")
result = cursor.fetchall()
print(result)

def hello():
    pass