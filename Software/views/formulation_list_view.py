import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


class FormulationListView:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.selected_row_id = None  # To keep track of the selected row

        # Create a frame to hold the table and buttons
        self.table_frame = ttk.Frame(self.parent_frame)
        self.table_frame.place(x=20, y=20, width=450, height = 500)

        # Create the Treeview (table)
        self.columns = ('ID', 'Name', 'Notes')  #this could all be parameterised!
        self.table = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
        self.table.heading('ID', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Notes', text='Notes')
        self.table.column("ID", width=50)  
        self.table.column("Name", width=120)  

        # Add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.place(relx=0, rely=0, relwidth = 0.9, relheight = 0.8)

        # Create a frame below the table for action buttons
        self.button_frame = ttk.Frame(self.parent_frame)
        self.new_button = ttk.Button(self.button_frame, text="New", state=tk.NORMAL)
        self.copy_button = tk.Button(self.button_frame, text="Copy", state=tk.DISABLED)
        self.delete_button = tk.Button(self.button_frame, text="Delete", state=tk.DISABLED)

        self.new_button.pack(side=tk.LEFT, padx=5)
        self.copy_button.pack(side=tk.LEFT, padx=5)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.button_frame.place(relx=0.2, rely = 0.92)
    
    def bind_row_selection(self, callback):
        """Expose a method for the presenter to bind the row selection event."""
        self.table.bind('<<TreeviewSelect>>', callback)

    def get_id_of_selected_row(self):
        """Helper method to retrieve the currently selected row's values."""
        selected_item = self.table.selection()
        if selected_item:
            print (self.table.item(selected_item[0], "values")[0])
            return self.table.item(selected_item[0], "values")[0]
            
        return None

    def show_formulations(self, data):
        # First clear table
        self.table.delete(*self.table.get_children())
        # Then restore rows from data
        for row in data:
            self.table.insert("", "end", values=(row['id'], row['name'], row['notes']))
        


    def enable_buttons(self):
            self.copy_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)

    def disable_buttons(self):
            self.copy_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def create_new(self):
        if self.selected_row_id:
            print(f"Viewing row with ID: {self.selected_row_id}")

class FormulationListPopupView(ttk.Frame):
    def __init__(self, master, save_callback):
        super().__init__(master)
        self.master = master
        self.save_callback = on_save_callback  # Callback function passed by Presenter
        self.master.title("Add New Item")
        self.master.geometry("300x200")
        
        # Variables for entries
        self.editable_field = tk.StringVar()
        self.dropdown1_value = tk.StringVar()
        self.dropdown2_value = tk.StringVar()
        
        # Create widgets
        ttk.Label(self, text="Editable Field:").grid(row=0, column=0, padx=10, pady=10)
        self.editable_entry = ttk.Entry(self, textvariable=self.editable_field)
        self.editable_entry.grid(row=0, column=1)

        ttk.Label(self, text="Dropdown 1:").grid(row=1, column=0, padx=10, pady=10)
        self.dropdown1 = ttk.Combobox(self, textvariable=self.dropdown1_value, values=["Option 1", "Option 2", "Option 3"])
        self.dropdown1.grid(row=1, column=1)

        ttk.Label(self, text="Dropdown 2:").grid(row=2, column=0, padx=10, pady=10)
        self.dropdown2 = ttk.Combobox(self, textvariable=self.dropdown2_value, values=["Option A", "Option B", "Option C"])
        self.dropdown2.grid(row=2, column=1)

        # Create buttons
        self.save_button = ttk.Button(self, text="Save", state=tk.DISABLED, command=self.save)
        self.save_button.grid(row=3, column=0, padx=10, pady=20)
        self.cancel_button = ttk.Button(self, text="Cancel", command=self.cancel)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=20)

        # Trace variables to enable save button if all fields are filled
        self.editable_field.trace("w", self.check_fields)
        self.dropdown1_value.trace("w", self.check_fields)
        self.dropdown2_value.trace("w", self.check_fields)

    def check_fields(self, *args):
        """Check if all fields are filled, enable Save button if valid."""
        if (self.editable_field.get().strip() and 
            self.dropdown1_value.get() and 
            self.dropdown2_value.get()):
            self.save_button.state(["!disabled"])
        else:
            self.save_button.state(["disabled"])

    def save(self):
        """Trigger the on_save_callback with collected data and close the pop-up."""
        self.save_callback(self.editable_field.get(), self.dropdown1_value.get(), self.dropdown2_value.get())
        self.master.destroy()

    def cancel(self):
        self.master.destroy()




