from dataclasses import dataclass

@dataclass
class Formulation:
    id: int = 0
    name: str = 'Unknown'
    notes: str = ''    

@dataclass
class FormulationDetail:
    id: int = 0
    name: str = 'Unknown'
    notes: str = ''    
    buffer_name: str = ''
    material_name: str = ''
    concentration_mmol: float = 0.0
    unit: int = 0


