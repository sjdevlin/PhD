import tkinter as tk
from tkinter import ttk


class GenericListView:
    def __init__(self, parent_frame, heading_list):
        self.parent_frame = parent_frame
        self.selected_row_id = None  # To keep track of the selected row

        # Create a frame to hold the table and buttons
        self.table_frame = ttk.Frame(self.parent_frame)
        self.table_frame.place(x=20, y=20, width=450, height = 500)

        # Create the Treeview (table)
        self.columns = ('ID', 'Name', 'Notes')  #this could all be parameterised!
        self.table = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
        self.table.heading('ID', text=heading_list[0])
        self.table.heading('Name', text=heading_list[1])
        self.table.heading('Notes', text=heading_list[2])
        self.table.column("ID", width=50)  
        self.table.column("Name", width=120)  

        # Add a scrollbar  NOT WORKING PLEASE FIX !
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

    def show_list(self, data):
        # First clear table
        self.table.delete(*self.table.get_children())
        # Then restore rows from data
        for row in data:
            self.table.insert("", "end", values=(row[0], row[1], row[2]))
        
    def enable_buttons(self):
            self.copy_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)

    def disable_buttons(self):
            self.copy_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def create_new(self):
         pass





