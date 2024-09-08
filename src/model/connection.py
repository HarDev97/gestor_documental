from psycopg2 import sql
from decouple import config
import psycopg2
import os


class Connection:
    def __init__(self):
        print("entro")
        print(config("PASSWORD"))

        self.connection = psycopg2.connect(
            user=config("USER"),
            password=config("PASSWORD"),
            host=config("HOST"),
            port=config("PORT"),
            database=config("DATABASE"),
        )
        print("met")
        data = self.read()
        print("Datos de la tabla usuarios:")
        for row in data:
            print(f"ID: {row[0]}, Usuario: {row[1]}")

    def read(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM usuarios")
        data = cur.fetchall()
        cur.close
        return data
