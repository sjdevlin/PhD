from models.formulation import Formulation

class FormulationListStore:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        query = "SELECT id, name, notes FROM Formulation"
        data = self.db.query(query)
        result = [Formulation(*row) for row in data]
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


class FormulationDetailStore:
    def __init__(self, db):
        self.db = db

    def get(self, formulation_id):
        query = """
        SELECT
            c.name AS component_name,
            c.notes AS component_notes,
            b.name AS buffer_name,
            m.name AS material_name,
            c.concentration_mmol AS concentration,
            fl.units AS units
        FROM
            FormulationLine fl
        JOIN
            Component c ON fl.component_id = c.id
        LEFT JOIN
            Buffer b ON c.buffer_id = b.id
        LEFT JOIN
            Material m ON c.material_id = m.id
        WHERE
            fl.formulation_id = %s
        """
        data = self.db.query(query, (formulation_id,))
        return (data)
        #insert logic to build formulation detail object
    
    def delete(self, formulation_line_id):
        query = "DELETE FROM FormulationLine WHERE id = ?"
        result = self.db.query(query, (formulation_line_id,))
        print (f"Single delete from the lines table: {result}")

    







