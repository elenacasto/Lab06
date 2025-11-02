import mysql
from mysql.connector import cursor
import mysql.connector

from database import DB_connect
from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:

        query = """
            SELECT *
            FROM automobile
        """

        conn = get_connection()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query)

            risultato = cursor.fetchall()
            cursor.close()
            conn.close()

            if not risultato:
                return None

            automobili = []
            for row in risultato:
                automobili.append(Automobile(*row))
            return automobili

        except mysql.connector.Error as err:
            print(f"Errore durante l'accesso al database {err}")
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """

        query = """
        SELECT *
        FROM automobile
        WHERE modello = %s 
        """
        conn = get_connection()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute(query, (modello,))
            risultato = cursor.fetchall()
            cursor.close()
            conn.close()

            if not risultato:
                return None

            automobili = []
            for row in risultato:
                automobili.append(Automobile(*row))
            return automobili

        except mysql.connector.Error as err:
            print(f"Errore durante l'accesso al database {err}")
            return None
