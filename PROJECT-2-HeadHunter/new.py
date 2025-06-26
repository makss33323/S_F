import pandas as pd
import psycopg2

import matplotlib.pyplot as plt
import seaborn as sns

import requests
from bs4 import BeautifulSoup

DBNAME = 'Skillfactory'
USER = 'skillfactory'
PASSWORD = 'cCkxxLVrDE8EbvjueeMedPKt'
HOST = '84.201.134.129'
PORT = 5432

connection = None  # Инициализация connection
cursor = None      # Инициализация cursor

try:
    connection = psycopg2.connect(
        dbname=DBNAME,
        user=USER,
        host=HOST,
        password=PASSWORD,
        port=PORT
    )
    cursor = connection.cursor()

    # --- Вставьте ваш SQL-запрос здесь ---
    query = "SELECT table_schema, table_name FROM information_schema.tables WHERE table_catalog = 'project_sql' AND table_schema NOT IN ('pg_catalog', 'information_schema');" # Запрос для получения всех таблиц и их схем
    # --- Вставьте ваш SQL-запрос здесь ---

    cursor.execute(query)

    # Если запрос возвращает данные (например, SELECT)
    results = cursor.fetchall() # Получить все строки
    for row in results:
        print(row)

    # Если запрос не возвращает данные (например, INSERT, UPDATE, DELETE),
    # можно использовать connection.commit() для сохранения изменений.
    # connection.commit()

except Exception as e:
    print(f"Ошибка при работе с базой данных: {e}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Соединение с базой данных закрыто.")