class FormulationDetailModel:
    def __init__(self, formulation_detail_store):
        self.formulation_detail_store = formulation_detail_store
        self.formulation_detail = []

    def get(self, row_id):   
        self.formulation_detail = self.formulation_detail_store.get(row_id)

    def delete(self, row_id):
        result = self.formulation_detail_store.delete(self.db, row_id)
        print (result)

