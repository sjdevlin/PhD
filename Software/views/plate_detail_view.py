import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


class PlateDetailView:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        # Create a canvas to display the plate image
        self.canvas = tk.Canvas(self.parent_frame, width=500, height=500, bg="white")
        self.canvas.pack()
    
    def show_plate_image(self, plate):

        self.plate = plate
        self.canvas.delete("all")  # Clear any previous drawings


        # Define the rectangle's top-left and bottom-right coordinates
        self.canvas.create_rectangle(0, 0, self.plate.width, self.length, outline="black", width=2)

        # Iterate through rows and columns to draw the shapes
        for row in range(self.plate.num_rows):
            for col in range(self.plate.num_columns):
                x1 = self.plate.centre_first_well_offset_x + col * self.plate.well_spacing_x
                y1 = self.plate.centre_first_well_offset_y + row * self.plate.well_spacing_y
                x2 = x1 + self.plate.well_dimension_x
                y2 = y1 + self.plate.well_dimension_y

                if self.plate.well_type == "square":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", fill="lightblue")
                elif shape_type == "circle":
                    self.canvas.create_oval(x1, y1, x2, y2, outline="blue", fill="lightblue")
                else:
                    self.display_error(f"Invalid shape type: {self.plate.well_type}")

    def display_error(self, message):
        """Show an error message in a pop-up dialog."""
        messagebox.showerror("Error", message)
