class GenericListModel:
    def __init__(self, object_store):
        self.object_store = object_store
        self.list = []

    def load(self):   
        self.list = self.object_store.get_all()

    def copy(self, row_id):
        result = (self.object_store.copy(row_id))
        print (result)

    def delete(self, row_id):
        result = self.object_store.delete(row_id)
        print (result)
