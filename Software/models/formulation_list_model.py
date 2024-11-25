class FormulationListModel:
    def __init__(self, formulation_list_store):
        self.formulation_list_store = formulation_list_store
        self.formulation = []

    def load_formulations(self):   
        self.formulation = self.formulation_list_store.get_all()

    def copy_formulation(self, row_id):
        result = (self.formulation_list_store.copy(row_id))
        print (result)

    def delete_formulation(self, row_id):
        result = self.formulation_list_store.delete(row_id)
        print (result)
