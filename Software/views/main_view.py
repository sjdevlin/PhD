import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox


class MainView:
    def __init__(self, root):
        self.root = root # Bare class is passed TK root widget.
        self.info_frame = ttk.Frame(self.root) # create new frame for detail stuff
        self.info_frame.place(x=190, y=20, width=400, height=560)
        self.detail_frame = ttk.Frame(self.root) # create new frame for detail stuff
        self.detail_frame.place(x=640, y=20, width=400, height=560)

        # Create the main sidebar frame
        self.create_sidebar()
        self.create_material_sidebar()
        self.create_imaging_sidebar()

    def create_sidebar(self):

        self.sidebar = ttk.Frame(self.root)

        self.component_button = ttk.Button(self.sidebar, text="Component")
        self.formulation_button = ttk.Button(self.sidebar, text="Formulation")
        self.annealing_button = ttk.Button(self.sidebar, text="Annealing Profile")
        self.experiment_button = ttk.Button(self.sidebar, text="Experiment")

        self.component_button.pack(fill=tk.X)
        self.formulation_button.pack(fill=tk.X) # format the button placement
        self.annealing_button.pack(fill=tk.X)
        self.experiment_button.pack(fill=tk.X)

        self.sidebar.place(x=20, y=50, width=150, height=150)


    def create_material_sidebar(self):
        
        self.material_sidebar = ttk.Frame(self.root)

        self.material_button = ttk.Button(self.material_sidebar, text="Material")
        self.material_button.pack(fill=tk.X)
        self.plate_button = ttk.Button(self.material_sidebar, text="Plate")
        self.plate_button.pack(fill=tk.X)

        self.buffer_button = ttk.Button(self.material_sidebar, text="Buffer")
        self.buffer_button.pack(fill=tk.X)

        self.material_sidebar.place(x=20, y=250, width=150, height=150)

    def create_imaging_sidebar(self):
        
        self.imaging_sidebar = ttk.Frame(self.root)

        self.camera_button = ttk.Button(self.imaging_sidebar, text="Camera")
        self.camera_button.pack(fill=tk.X)

        self.camera_setting_button = ttk.Button(self.imaging_sidebar, text="Camera Setting")
        self.camera_setting_button.pack(fill=tk.X)

        self.microscope_button = ttk.Button(self.imaging_sidebar, text="Microscope")
        self.microscope_button.pack(fill=tk.X)

        self.imaging_sidebar.place(x=20, y=400, width=150, height=150)



    def display_error(self, message):
        """Show an error message in a pop-up dialog."""
        messagebox.showerror("Error", message)
