from database import Database
from app import Application

def main():
    # Create Database and Table
    db = Database()
    print("Creating Database : Complete")

    # Open GUI
    print("Launching App : Pending")
    app = Application()
    app.mainloop()
    print("Launching App : Complete")

if __name__ == "__main__":
    main()