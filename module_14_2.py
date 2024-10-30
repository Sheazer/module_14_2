import sqlite3 as sql

connection = sql.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
''')
cursor.execute("DELETE FROM Users")
#Добавляем 30 записей в дб
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'username{i}', f'example{i}@gmail.com', i * 10, 1000))

#Изменаем баланс у каждого второго
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 != 0")

#Удаляем каждую третью запись с бд
cursor.execute("DELETE FROM Users WHERE (id-1) % 3 == 0")

#Выводим на экран
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
result = cursor.fetchall()

for user in result:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

cursor.execute("DELETE FROM Users WHERE id == 6")
cursor.execute("SELECT COUNT(*) FROM Users")
x = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
sm = cursor.fetchone()[0]

print(sm/x)


connection.commit()
connection.close()
