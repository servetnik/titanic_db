import sqlite3

con = sqlite3.connect('titanic.db')
cur = con.cursor()

#Дети
cur.execute("""SELECT name, age FROM people WHERE age < '18'""")
result1 = cur.fetchall()
print(result1)

#Палубная команда
cur.execute("""SELECT * FROM people WHERE job LIKE 'ship%' OR job LIKE 'deck%' """)
result2 = cur.fetchall()
print(result2)
con.commit()

#Кол-во выживших
cur.execute("""SELECT COUNT(name) FROM people WHERE survived = 'TRUE'""")
result3 = cur.fetchall()
print(result3)
con.commit()

#Кол-во невыживших
cur.execute("""SELECT COUNT(name) FROM people WHERE survived = 'FALSE'""")
result3 = cur.fetchall()
print(result3)
con.commit()

#Всего
cur.execute("""SELECT COUNT(name)FROM people""")
result3 = cur.fetchall()
print(result3)
con.commit()
