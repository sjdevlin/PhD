import sys
import yaml
import tkinter as tk
from presenters.main_presenter import MainPresenter
from views.main_view import MainView
from database.database import Database

class Config:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.config = yaml.safe_load(file)

    def get(self, section, key):
        return self.config.get(section, {}).get(key)

import yaml
import sys

class Config:
    def __init__(self, filename):
        try:
            with open(filename, 'r') as file:
                self.config = yaml.safe_load(file)
                if self.config is None:
                    print ("Error opening the file.")
                    sys.exit(1)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            sys.exit(1)

    def get(self, section, key):
        return self.config.get(section, {}).get(key)


# check config file argument is provided
if len(sys.argv) < 2:
    print("Usage: python config.py <config_file>")
    sys.exit(1)

config_file = sys.argv[1]
config = Config(config_file)

db_name = config.get('Settings', 'DB_NAME')
db_user = config.get('Settings', 'DB_USER')
db_password = config.get('Settings', 'DB_PASSWORD')
print(f"Database: {db_name}  User: {db_user}")

# Initialize the main window
root = tk.Tk()
root.title("System X")
root.geometry("1200x600")

# Database connection
db = Database(db_name,db_user,db_password)

# Initialize the view and presenter
main_view = MainView(root)
presenter = MainPresenter(main_view, db)

root.mainloop()
