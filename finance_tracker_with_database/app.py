import tkinter as tk
from tkinter import ttk
import datetime

from finance import Finance

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finance Tracker")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        # self
        
        # Tree
        tree_view = TreeFrame(self)

        # Add side frmae
        side_frame = SideBarFrame(self,tree_view)

        # Add Options Frame
        options_frame = OptionsFrame(self,tree_view,side_frame)

        

        side_frame.grid(row=0,column=0,rowspan=2,sticky="sn")
        options_frame.grid(row=0,column=1,columnspan=2,sticky="nsew")
        tree_view.grid(row=1,column=1,columnspan=2,sticky="nsew")
        
class SideBarFrame(ttk.Frame):
    def __init__(self,parent,tree_view):
        self.tree_view = tree_view
        super().__init__(parent)
        self.f = Finance()
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Main Label
        self.main_label = ttk.Label(self,text="EXPENSE TRACKER",font=20)
        self.main_label.grid(row=0,column=0,columnspan=2)

        # Sub Label
        self.sub_label = ttk.Label(self,text="Data Entry Frame")
        self.sub_label.grid(row=1,column=0,columnspan=2)

        # Date
        self.date_label = ttk.Label(self,text="Date")
        self.date_label.grid(row=2,column=0)

        self.date_entry = ttk.Entry(self)
        self.date_entry.grid(row=2,column=1)

        # Amount
        self.amount_label = ttk.Label(self,text="Amount")
        self.amount_label.grid(row=3,column=0)

        self.amount_entry = ttk.Entry(self)
        self.amount_entry.grid(row=3,column=1)

        # Category
        self.category_label = ttk.Label(self,text="Category")
        self.category_label.grid(row=4,column=0)

        self.category_entry = ttk.Entry(self)
        self.category_entry.grid(row=4,column=1)

        # Description
        self.description_label = ttk.Label(self,text="Description")
        self.description_label.grid(row=5,column=0)

        self.description_entry = ttk.Entry(self)
        self.description_entry.grid(row=5,column=1)

        # Buttons
        self.add_button = ttk.Button(self,text="Add Expense",width=20,command=self.add_to_db)
        self.add_button.grid(row=6,column=0,columnspan=2)

        self.reset_fields_button = ttk.Button(self,text="Reset the fields",width=20,command=self.clear_fields)
        self.reset_fields_button.grid(row=7,column=0,columnspan=2) 
    
    def add_to_db(self,_event=None):
        # Get all the data from fields
        amount = self.amount_entry.get()
        date = datetime.date.today()
        description = self.description_entry.get()
        category = self.category_entry.get()

        self.f.add_expenses((amount,category,date, description))
        self.tree_view.reload_tree()
        print("Added new Expense")
        self.clear_fields()

    def clear_fields(self,_event=None):
        self.amount_entry.delete(0,tk.END)
        self.date_entry.delete(0,tk.END)
        self.description_entry.delete(0,tk.END)
        self.category_entry.delete(0,tk.END)

    def add_to_fields(self,data):
        id,amount,category,date,description = data
        self.clear_fields()
        
        self.amount_entry.insert(0,amount)
        self.date_entry.insert(0,date)
        self.description_entry.insert(0,description)
        self.category_entry.insert(0,category)

class OptionsFrame(ttk.Frame):
    def __init__(self,parent,tree,side_bar):
        super().__init__(parent)
        self.tree = tree.get_tree()
        self.tree_view = tree
        self.side_bar = side_bar
        self.f = Finance()

        self.config(padding=10)
        # Buttons
        self.view_expense_btn = ttk.Button(self,text="View Selected Expense Details",width=30,command=self.view_expense)
        self.view_expense_btn.grid(row=0,column=0)

        self.edit_expense_btn = ttk.Button(self,text="Edit Selected Expense",width=30)
        self.edit_expense_btn.grid(row=0,column=1)

        self.export_btn = ttk.Button(self,text="Export as csv",width=30)
        self.export_btn.grid(row=0,column=2)

        self.delete_expense_btn = ttk.Button(self,text="Delete Selected Expense",width=30)
        self.delete_expense_btn.grid(row=1,column=0)

        self.delete_all_expenses = ttk.Button(self,text="Delete All Expenses",width=30,command=self.delete_all_expenses)
        self.delete_all_expenses.grid(row=1,column=1)

    def view_expense(self):
        selected_row = self.tree.selection()
        if selected_row:
            item_data = self.tree.item(selected_row[0], "values")
            self.side_bar.add_to_fields(item_data)

    def delete_all_expenses(self):
        self.f.delete_all_entries()
        self.f.recreate_table()
        self.tree_view.reload_tree()
        

class TreeFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.f = Finance()

        # self.config(text="Previous Purchases")
        self.cols = ("id","amount","category", "date","description")
        self.treeView = ttk.Treeview(self,columns=self.cols,show="headings")

        self.treeView.heading("id",text="ID")
        self.treeView.heading("amount",text="Amount($)")
        self.treeView.heading("category",text="Category")
        self.treeView.heading("date",text="Date")
        self.treeView.heading("description",text="Description")

        self.treeView.grid(row=0,column=0,sticky="nsew")

        self.reload_tree()

    def reload_tree(self):
        # Clear the tree first
        for item in self.treeView.get_children():
            self.treeView.delete(item)
        data = self.f.get_all_values()
        for info in data:
            # Add all the values back to the tree again
            self.treeView.insert("","end",values=info)

    def get_tree(self):
        return self.treeView

if __name__ == "__main__":
    main()