import sqlite3 as sql


class Database:
    def __init__(self):
        self.create_table()

    def create_table(self):
        conn, c = self.setup_conn()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
            user_id text UNIQUE,
            user_name text UNIQUE
            );
            """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS urls
            (
            short_url text UNIQUE,
            actual_url text
            )
        """)
        self.close_conn(conn)

    def setup_conn(self):
        conn = sql.connect("./data/url_service.db")
        c = conn.cursor()
        return conn, c

    def close_conn(self, conn):
        conn.close()

    def add_user(self, user_name, user_id):
        try:
            conn, c = self.setup_conn()
            c.execute(f"""
                INSERT INTO users VALUES ("{user_name}","{user_id}")
            """)
            conn.commit()
            print("[Adding User] : Success")

        except sql.IntegrityError as e:
            print(f"[Adding User] : Failed (User Exists)\n\t{e}")

        except sql.OperationalError as e:
            print(f"[ Adding User ] : Failed \n\t{e}")

        self.close_conn(conn)

    def show_all_users(self):
        try:
            conn, c = self.setup_conn()
            c.execute(f"""
                SELECT * FROM users
                """)
            print("[Show Users] : Success")
            return c.fetchall()

        except Exception as e:
            print("[Show Users] : Failed")
        self.close_conn(conn)

    def show_all_urls(self):
        try:
            conn, c = self.setup_conn()
            c.execute(f"""
                SELECT * FROM urls
                """)
            print("[Show Urls] : Success")
            return c.fetchall()

        except Exception as e:
            print("[Show Urls] : Failed")
        self.close_conn(conn)

    def find_user(self, user_id):
        try:
            conn, c = self.setup_conn()
            c.execute(f"""
                SELECT * FROM users WHERE
                user_id={user_id}
                """)
            return c.fetchall()

        except Exception as e:
            print("User Not Found")
            return None

        self.close_conn(conn)

    def add_new_url(self, short_url, ori_url):
        try:
            conn, c = self.setup_conn()
            c.execute(f"""
            INSERT INTO urls VALUES ("{short_url}","{ori_url}")
            """)
            conn.commit()
        except sql.IntegrityError as e:
            print(f"{e}")
        self.close_conn(conn)


if __name__ == "__main__":
    db = Database()
    db.add_user("Xenon", "ndj2")
    print(db.show_all_users())
    print(db.find_user('ndj2'))
