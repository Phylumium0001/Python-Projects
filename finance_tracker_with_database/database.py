import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("my_db.db")
        self.c = self.conn.cursor()
        # Create the table
        self.c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT,
                date TEXT,
                description TEXT
            );""")
        

    def add_purchase(self,amount, category,date,description):
        with self.conn:
            self.c.execute(f"INSERT INTO expenses (amount,category,date,description) VALUES ('{amount}','{category}','{date}','{description}')")

    def get_all_data(self):
        with self.conn:
            values = self.c.execute("SELECT * FROM expenses").fetchall()
            return values
        
    def sort_by(self, parameter):
        with self.conn:
            order = self.c.execute(f"SELECT * FROM expenses ORDER BY {parameter} ASC")
            return order.fetchall()
        
    def update_amount(self,id,amount):
        with self.conn:
            self.c.execute(f"UPDATE expenses SET amount={amount} where id={id}")

    def update_date(self,id,date):
        with self.conn:
            self.c.execute(f"UPDATE expenses SET date='{date}' where id={id}")

    def update_description(self,id,description):
        with self.conn:
            self.c.execute(f"UPDATE expenses SET description='{description}' where id={id}")

    def update_category(self,id,category):
        with self.conn:
            self.c.execute(f"UPDATE expenses SET category='{category}' where id={id}")

    def get_all_amount_trans(self):
        with self.conn:
            all_trans = self.c.execute("SELECT amount FROM expenses")
            return all_trans.fetchall()
        
    def get_amount_by_category(self,category):
        with self.conn:
            cat_trans = self.c.execute(f"SELECT amount FROM expenses WHERE category='{category}'")
            return cat_trans.fetchall()
        
if __name__ == "__main__":
    db = Database()
    # db.add_purchase(12,"New","21/01/2023","NewBook")
    db.update_category(1,"Work")
    for data in db.get_amount_by_category("Food"):
        print(data)

    # print(db.get_all_data())