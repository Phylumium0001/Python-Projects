import os
import psycopg2
from psycopg2 import sql


class Database:
    def __init__(self):
        # The connection string is read from the environment variable
        self.DATABASE_URL = os.environ.get("DATABASE_URL")
        if not self.DATABASE_URL:
            raise RuntimeError("DATABASE_URL environment variable not set.")
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
                    short_url TEXT PRIMARY KEY,
                    actual_url TEXT NOT NULL
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
                sql.SQL("INSERT INTO urls (short_url, actual_url) VALUES (%s, %s)"),
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
                sql.SQL("SELECT actual_url FROM urls WHERE short_url = %s"),
                (short_url,)
            )
            result = c.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"[Find URL] : Failed \n\t{e}")
            return None
        finally:
            self.close_conn(conn)

# Note: The `users` table and related functions were removed for brevity,
# as they were not part of the core URL shortening logic.
# You can adapt them using the same principles.
