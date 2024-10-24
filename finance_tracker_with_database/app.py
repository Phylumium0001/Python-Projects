import tkinter as tk
from tkinter import ttk


def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Finance App")
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)

        frame1 = InsertDetailsFrame(self)
        frame1.grid(row=0,column=0,pady=10,sticky="wn")

        frame2 = TreeViewFrame(self)
        frame2.grid(row=1,column=0,sticky="nsew")

class InsertDetailsFrame(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.config(text="Add Purchase")

        self.amount_label = ttk.Label(self,text="Amount($)")
        self.amount_label.grid(row=0,column=0,ipadx=2)

        self.amount_entry = ttk.Entry(self)
        self.amount_entry.grid(row=0,column=1)
        
        self.empty_space = ttk.Label(self)
        self.empty_space.grid(row=0,column=2,padx=15)

        self.category_label = ttk.Label(self,text="Category")
        self.category_label.grid(row=0,column=3,padx=5)

        self.categories = ttk.Menubutton(self)
        self.categories.grid(row=0,column=4)

        self.empty_space2 = ttk.Label(self)
        self.empty_space2.grid(row=0,column=5,padx=15)

        self.add_purchase_btn = ttk.Button(self, text="Add")
        self.add_purchase_btn.grid(row=0,column=6,padx=5)

        self.description_label = ttk.Label(self,text="Description")
        self.description_label.grid(row=1,column=0,padx=10)

        self.description = ttk.Entry(self,width=20)
        self.description.grid(row=1,column=1,columnspan=6,sticky="ew")


class TreeViewFrame(ttk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.config(text="Previous Purchases")
        
        self.treeView = ttk.Treeview(self,columns=["Date","Category", "Amount($)","Description"])
        self.treeView.grid(row=0,column=0,sticky="nsew")

if __name__ == "__main__":
    main()