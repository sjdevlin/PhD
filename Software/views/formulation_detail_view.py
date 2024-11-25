import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


class FormulationDetailView:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame

        self.selected_row_id = None  # To keep track of the selected row

        # Create a frame to hold the table and buttons
        self.table_frame = ttk.Frame(self.parent_frame)
        self.table_frame.place(x=20, y=20, width=500, height = 500)

        # Create the Treeview (table)
        self.columns = ('Component', 'Notes','Units')  #this could all be parameterised!
        self.table = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')
        self.table.heading('Component', text='Component')
        self.table.heading('Notes', text='Notes')
        self.table.heading('Units', text='Units')

        self.table.column("Component", width=50)  
        self.table.column("Notes", width=160)  

        # Add a scrollbar
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.place(relx=0, rely=0, relwidth = 0.9, relheight = 0.8)

        # Create a frame below the table for action buttons
        self.button_frame = ttk.Frame(self.parent_frame)

        self.add_button = ttk.Button(self.button_frame, text="Add", state=tk.NORMAL)
        self.delete_button = tk.Button(self.button_frame, text="Delete", state=tk.DISABLED)
        self.save_button = tk.Button(self.button_frame, text="Save", state=tk.DISABLED)

        self.add_button.pack(side=tk.LEFT, padx=5)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.button_frame.place(relx=0.2, rely = 0.92)
    
    def bind_row_selection(self, callback):
        """Expose a method for the presenter to bind the row selection event."""
        self.table.bind('<<TreeviewSelect>>', callback)

    def get_id_of_selected_row(self):
        """Helper method to retrieve the currently selected row's values."""
        selected_item = self.table.selection()
        print(selected_item)
        if selected_item:
            print(self.table.item(selected_item[0], "values")[0])
            return self.table.item(selected_item[0], "values")[0]
        return None

    def show_formulations(self, data):
        """Populate the Treeview with data."""
        self.table.delete(*self.table.get_children())
        for row in data:
            self.table.insert('', 'end', values=(row[0], row[1], row[5]))

    def enable_buttons(self):
            self.delete_button.config(state=tk.NORMAL)

    def create_new(self):
        if self.selected_row_id:
            print(f"Viewing row with ID: {self.selected_row_id}")

    def copy_row(self):
        if self.selected_row_id:
            print(f"Copying row with ID: {self.selected_row_id}")

    def delete_row(self):
        if self.selected_row_id:
            print(f"Deleting row with ID: {self.selected_row_id}")
            # Remove the row from the Treeview after deletion
            selected = self.table.selection()
            for item in selected:
                self.table.delete(item)
            # Disable buttons after deletion
            self.copy_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

    def toggle_button_color(self, button):
        """Toggle the color of the active button."""
        button.config(bg='black', fg='white')

    def reset_button_color(self, button):
        """Reset the color of the inactive buttons."""
        button.config(bg='gray', fg='black')

    def display_error(self, message):
        """Show an error message in a pop-up dialog."""
        messagebox.showerror("Error", message)
