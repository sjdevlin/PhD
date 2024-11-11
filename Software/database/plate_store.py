from models.plate import Plate

class PlateStore:
    def __init__(self, db):
        self.db = db

    def get_all(self):

        query = """SELECT 
        id,
        name,
        notes,
        width,
        length,
        num_rows,
        num_columns,
        centre_first_well_offset_x,
        centre_first_well_offset_y,
        well_type,
        well_dimension_x,
        well_dimension_y,
        well_spacing_x, 
        well_spacing_y,
        min_well_volume,
        max_well_volume
        
        FROM Plate"""

        data = self.db.query(query)
        result = []
        for row in data:
            result.append(Plate())
        return (result)
    
    def copy(self, row_id):
        query = """        
        INSERT INTO Formulation (name,notes, is_master)
        SELECT CONCAT(name, ' (copy)'), notes, is_master
        FROM Formulation
        WHERE id = %s;"""
        result = self.db.query(query, (row_id,))
        print (f"First Insert Result: {result}")
      
        query = "SELECT LAST_INSERT_ID()"
        new_id = self.db.query(query)[0][0]
        print (f"Last ID inserted: {new_id}")

        query = """
        INSERT INTO FormulationLine (formulation_id, component_id, units)
        SELECT %s, component_id, units
        FROM FormulationLine
        WHERE formulation_id = %s
        """
        new_id

        result = self.db.query(query, (new_id,row_id))
        print (f"Second Insert Result: {result}")


    def delete(self, row_id):
        query = "DELETE FROM FormulationLine WHERE formulation_id = %s"
        result = self.db.query(query, (row_id,))
        print (f"first delete, from the lines table: {result}")

        query = "DELETE FROM Formulation WHERE id = %s"
        result = self.db.query(query, (row_id,))
        print (f"second delete, from the formulation table: {result}")
    
    def save(self, formulation):
        query = "INSERT INTO Formulation (name, notes) VALUES %s"
        result = self.db.query(query, formulation)
        return (result)


