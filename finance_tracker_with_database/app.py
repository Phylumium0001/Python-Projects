import tkinter as tk
from tkinter import ttk
import datetime

from finance import Finance

def main():
    app = Application()
    app.mainloop()

# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         # Finance instance (API)

#         self.title("Finance App")
#         self.rowconfigure(1,weight=1)
#         self.columnconfigure(0,weight=1)

#         frame2 = TreeViewFrame(self)
#         frame1 = InsertDetailsFrame(self, frame2)

#         frame1.grid(row=0,column=0,ipadx=10,ipady=10,sticky="wn")

#         frame2.grid(row=1,column=0,ipadx=10,ipady=10,sticky="nsew")


# class InsertDetailsFrame(ttk.LabelFrame):
#     def __init__(self,parent,tree):
#         self.style = ttk.Style()
#         self.style.theme_use("clam")

#         self.tree = tree
#         self.f = Finance()
#         super().__init__(parent)
#         self.config(text="Add Purchase")

#         self.amount_label = ttk.Label(self,text="Amount($)")
#         self.amount_label.grid(row=0,column=0)

#         self.amount_entry = ttk.Entry(self)
#         self.amount_entry.grid(row=0,column=1)
        
#         self.empty_space = ttk.Label(self)
#         self.empty_space.grid(row=0,column=2,padx=15)

#         self.category_label = ttk.Label(self,text="Category")
#         self.category_label.grid(row=0,column=3,padx=5)

#         self.categories = ttk.Entry(self)
#         self.categories.grid(row=0,column=4)

#         self.empty_space2 = ttk.Label(self)
#         self.empty_space2.grid(row=0,column=5,padx=15)

#         self.add_purchase_btn = ttk.Button(self, text="Add",command=self.submit_expense)
#         self.add_purchase_btn.grid(row=0,column=6,pady=10)

#         self.description_label = ttk.Label(self,text="Description")
#         self.description_label.grid(row=1,column=0,ipady=10,sticky="s")

#         self.description_entry = ttk.Entry(self,width=20)
#         self.description_entry.grid(row=1,column=1,columnspan=6,ipady=5,sticky="ews")


#     def submit_expense(self,_event=None):
#         # Get all the value present in the fields
#         amount = self.amount_entry.get()
#         category = self.categories.get()

#         # Date is automatically calc for
#         date = datetime.date.today()
#         description = self.description_entry.get()

#         self.f.add_expenses([amount, category,date,description])
#         print("Added a new value")
#         self.amount_entry.delete(0,tk.END)
#         self.description_entry.delete(0,tk.END)

#         self.tree.reload_tree()


# class TreeViewFrame(ttk.LabelFrame):
#     def __init__(self,parent):
#         super().__init__(parent)
#         self.f = Finance()
#         self.rowconfigure(0,weight=1)
#         self.columnconfigure(0,weight=1)
#         self.config(text="Previous Purchases")
#         self.cols = ("id","amount","category", "date","description")
#         self.treeView = ttk.Treeview(self,columns=self.cols,show="headings")

#         self.treeView.heading("id",text="ID")
#         self.treeView.heading("amount",text="Amount($)")
#         self.treeView.heading("category",text="Category")
#         self.treeView.heading("date",text="Date")
#         self.treeView.heading("description",text="Description")

#         self.treeView.grid(row=0,column=0,sticky="nsew")

#         self.reload_tree()

#     def reload_tree(self):
#         # Clear the tree first
#         for item in self.treeView.get_children():
#             self.treeView.delete(item)
#         data = self.f.get_all_values()
#         for info in data:
#             # Add all the values back to the tree again
#             self.treeView.insert("","end",values=info)

# class FilterFrame(ttk.Frame):
#     def __init__(self,parent):
#         super().__init__(parent)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finance Tracker")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        # self
        

        # Add side frmae
        side_frame = SideBarFrame(self)

        # Add Options Frame
        options_frame = OptionsFrame(self)

        # Tree
        tree_view = TreeFrame(self)

        side_frame.grid(row=0,column=0,rowspan=2,sticky="sn")
        options_frame.grid(row=0,column=1,columnspan=2,sticky="nsew")
        tree_view.grid(row=1,column=1,columnspan=2,sticky="nsew")
        
class SideBarFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
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
        self.date_label = ttk.Label(self,text="Category")
        self.date_label.grid(row=4,column=0)

        self.date_entry = ttk.Entry(self)
        self.date_entry.grid(row=4,column=1)

        # Description
        self.description_label = ttk.Label(self,text="Description")
        self.description_label.grid(row=5,column=0)

        self.description_entry = ttk.Entry(self)
        self.description_entry.grid(row=5,column=1)

        # Buttons
        self.add_button = ttk.Button(self,text="Add Expense",width=20)
        self.add_button.grid(row=6,column=0,columnspan=2)

        self.reset_fields_button = ttk.Button(self,text="Reset the fields",width=20)
        self.reset_fields_button.grid(row=7,column=0,columnspan=2) 
        

class OptionsFrame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.config(padding=10)
        # Buttons
        self.view_expense_btn = ttk.Button(self,text="View Selected Expense Details",width=30)
        self.view_expense_btn.grid(row=0,column=0)

        self.edit_expense_btn = ttk.Button(self,text="Edit Selected Expense",width=30)
        self.edit_expense_btn.grid(row=0,column=1)

        self.export_btn = ttk.Button(self,text="Export as csv",width=30)
        self.export_btn.grid(row=0,column=2)

        self.delete_expense_btn = ttk.Button(self,text="Delete Selected Expense",width=30)
        self.delete_expense_btn.grid(row=1,column=0)

        self.delete_all_expenses = ttk.Button(self,text="View Selected Expense Details",width=30)
        self.delete_all_expenses.grid(row=1,column=1)

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

if __name__ == "__main__":
    main()