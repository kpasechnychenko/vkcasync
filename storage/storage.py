import sqlite3
from contextlib import closing


class Storage:
    """
    Represents simple storage for application settings
    """
    def __init__(self):
        query = "CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY AUTOINCREMENT,key TEXT, value TEXT)"
        conn, cursor = self.__get_cursor()
        with closing(conn) as c:
            with closing(cursor) as cur:
                cur.execute(query)
        pass

    def __get_cursor(self):
        conn = sqlite3.connect("vkcasync.db")
        return conn, conn.cursor()

    def get(self, key):
        query = "SELECT value FROM settings WHERE key = ? LIMIT 1"
        conn, cursor = self.__get_cursor()
        with closing(conn) as c:
            with closing(cursor) as cur:
                result = (cur.execute(query, [key])).fetchone()
                if result is None:
                    return None
                return result[0]
        pass

    def set(self, key, value):
        query_insert = "INSERT INTO settings(key, value) VALUES(?, ?)"
        query_update = "UPDATE settings SET value = ? WHERE key = ?"
        val = self.get(key)
        conn, cursor = self.__get_cursor()
        if val is not None:
            with closing(conn) as c:
                with closing(cursor) as cur:
                    cur.execute(query_update, (value, key))
                    c.commit()
        else:
            with closing(conn) as c:
                with closing(cursor) as cur:
                    cur.execute(query_insert, (key, value))
                    c.commit()
        pass

    def delete(self, key):
        query = "DELETE FROM settings WHERE key = ?"
        conn, cursor = self.__get_cursor()
        with closing(conn) as c:
            with closing(cursor) as cur:
                cur.execute(query, [key])
                c.commit()
        pass
