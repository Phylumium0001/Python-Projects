import os
import psycopg2
from psycopg2 import sql


class Database:
    def __init__(self):
        # The connection string is read from the environment variable
        self.DATABASE_URL = os.environ.get("DATABASE_URL")
        if not self.DATABASE_URL:
            # Fallback for local development
            self.DATABASE_URL = "postgresql://postgres@localhost/short_url_service"
        self.create_tables()

    def setup_conn(self):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(self.DATABASE_URL)
        return conn, conn.cursor()

    def close_conn(self, conn):
        if conn:
            conn.close()

    def create_tables(self):
        conn, c = None, None
        try:
            conn, c = self.setup_conn()
            # Use parameterized queries to create tables securely
            c.execute("""
                CREATE TABLE IF NOT EXISTS urls (
                    short_url_code TEXT PRIMARY KEY,
                    actual_url TEXT NOT NULL,
                    num_visits INTEGER DEFAULT 0
                );
            """)
            conn.commit()
            print("[Database] : Tables created successfully.")
        except Exception as e:
            print(f"[Database] : Failed to create tables: {e}")
        finally:
            self.close_conn(conn)

    def add_new_url(self, short_url, ori_url):
        conn, c = None, None
        try:
            conn, c = self.setup_conn()
            # IMPORTANT: Use parameterized query to prevent SQL injection
            c.execute(
                sql.SQL(
                    "INSERT INTO urls (short_url_code, actual_url) VALUES (%s, %s)"),
                (short_url, ori_url)
            )
            conn.commit()
            print("[Adding URL] : Success")
        except psycopg2.IntegrityError:
            print("[Adding URL] : Failed (URL Exists)")
        except Exception as e:
            print(f"[Adding URL] : Failed \n\t{e}")
        finally:
            self.close_conn(conn)

    def find_url(self, short_url):
        conn, c = None, None
        try:
            conn, c = self.setup_conn()
            # Use parameterized query for safe searching
            c.execute(
                sql.SQL("SELECT * FROM urls WHERE short_url_code = %s"),
                (short_url,)
            )
            result = c.fetchone()
            # print(result)
            if result:
                return result
            else:
                return None
        except Exception as e:
            print(f"[Find URL] : Failed \n\t{e}")
            return None
        finally:
            self.close_conn(conn)

    def get_all_url(self):
        conn, c = None, None
        try:
            conn, c = self.setup_conn()
            # Use parameterized query for safe searching
            c.execute(sql.SQL("SELECT * FROM urls"))
            result = c.fetchall()
            # Always return a list, even if it's empty, instead of None
            print(result)
            return result if result is not None else []

        except Exception as e:
            print(f"[All Urls]{e}")
            return []  # Return an empty list on error
        finally:
            self.close_conn(conn)

    def increment_visit_count(self, short_url):
        conn, c = None, None
        try:
            conn, c = self.setup_conn()
            c.execute(
                sql.SQL(
                    "UPDATE urls SET num_visits = num_visits + 1 WHERE short_url_code = %s"),
                (short_url,)
            )
            conn.commit()
            print(f"[Visit Count] : Incremented count for {short_url}")
        except Exception as e:
            print(f"[Visit Count] : Failed to increment count: {e}")
        finally:
            self.close_conn(conn)


if __name__ == "__main__":
    db = Database()
    print(db.get_all_url())
