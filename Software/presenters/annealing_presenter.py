from presenters.base_presenter import BasePresenter
from views.formulation_detail_view import FormulationDetailView
from views.formulation_list_view import FormulationListView
from views.formulation_list_view import FormulationListPopupView

class AnnealingPresenter:

    def __init__(self, list_view, detail_view, list_model, detail_model):
        self.list_view = list_view
        self.detail_view = detail_view
        self.list_model = list_model
        self.detail_model = detail_model
        self.list_view.bind_row_selection(self.on_list_row_selected) # this gives a call back to the view
        self.detail_view.bind_row_selection(self.on_detail_row_selected) # this gives a call back to the view
        self.refresh_view()
        self.list_view.copy_button.config(command=self.copy_formulation)
        self.list_view.delete_button.config(command=self.delete_formulation)
        self.list_view.new_button.config(command=self.add_new)

    def add_new(self):
        self.list_view.add_new_popup(self.on_save)

    def on_save(self, editable, dropdown1, dropdown2):
        """Handles the save action triggered from the popup."""
        self.model.add_formulation(editable, dropdown1, dropdown2)
        print(f"Formulation saved: {editable}, {dropdown1}, {dropdown2}")


    def refresh_view(self):
        self.selected_row = None
        self.list_model.load_formulations()
        data = [{'id': f.id, 'name': f.name, 'notes': f.notes} 
            for f in self.list_model.formulation]
        print (data)
        self.list_view.show_formulations(data)

    def copy_formulation(self):
        # Handle the logic for copying a formulation
        self.list_model.copy_formulation(self.selected_row)
        self.refresh_view()  # Reload formulations to show the updated list

    def delete_formulation(self):
        # Handle the logic for deleting a formulation
        self.list_model.delete_formulation(self.selected_row)
        self.refresh_view()  # Reload formulations to show the updated list
        self.list_view.disable_buttons()

    def on_list_row_selected(self, event):
        """This method handles the row selection logic."""
        self.selected_row = self.list_view.get_id_of_selected_row()
        if self.selected_row:
            self.list_view.enable_buttons()
            self.view_formulation(self.selected_row)

    def on_detail_row_selected(self, event):
        """This method handles the row selection logic."""
        selected_row = self.detail_view.get_id_of_selected_row()
        if selected_row:
            self.detail_view.enable_buttons()
            print ("Row Selected")

    def view_formulation(self, formulation_id):
        # Handle the logic for viewing a formulation
        data = self.detail_model.get(formulation_id)
        data = (self.detail_model.formulation_detail)
        print (data)
        self.detail_view.show_formulations(data)

