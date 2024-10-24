from database import Database

class Finance:
    def __init__(self):
        # Initialize databas
        self.db = Database()
        
    
    def get_all_values(self):
        return self.db.get_all_data()
    
    def add_expenses(self,values=()):
        if len(values) != 0:
            amount, category,date,description = values
            self.db.add_purchase(amount, category,date,description) 

    def get_all_values(self):
        return self.db.get_all_data()

    def get_total_amount_spent(self):
        self.all_trans = self.db.get_all_amount_trans()
        total = 0
        for i in self.all_trans:
            total += i[0]
        return total
            
    def get_total_amount_by_category(category):
        pass

if __name__ == "__main__":
    f = Finance()
    f.add_expenses([20,"Food","12/02/2024","Bought"])
    values = f.get_all_values()
    print(values)
    f.get_total_amount_spent()