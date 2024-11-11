import tkinter as tk
from tkinter import ttk




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

