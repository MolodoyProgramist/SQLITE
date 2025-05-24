import os
import sqlite3

# Создаем папку, если её нет
os.makedirs('db', exist_ok=True)

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO expenses (id, age, name, grade) VALUES(1, 13, 'Андрей', '6 класе')"""
    query2 = """INSERT INTO expenses (id, age, name, grade) VALUES(2, 14, 'Илья', '7 класе')"""
    query3 = """INSERT INTO expenses (id, age, name, grade) VALUES(3, 12, 'Макс', '6 класе')"""
    query4 = """INSERT INTO expenses (id, age, name, grade) VALUES(4, 15, 'Лев', '8 класе')"""
    query5 = """INSERT INTO expenses (id, age, name, grade) VALUES(5, 16, 'Ваня', '8 класе')"""
    cursor.execute(query)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    db.commit()

#query = """CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT, age INTEGER, grade TEXT)""" #создание таблицы и столбцо в ней