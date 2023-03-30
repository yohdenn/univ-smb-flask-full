from flask import Flask
from mysql.connector import DataBase, InterfaceError, connect

def connexion(host: str, database: str, login: str, pwd: str):
    try:
        cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=pwd,
            database=database,
        )
        print(f"La connexion à la base de donnée est effectuée")
        return cnx
    except mysql.connector.Error as err:
        print (f"Connexion de connexion à la base de données: {err}")