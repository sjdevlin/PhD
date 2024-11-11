from dataclasses import dataclass
from enum import Enum

class WellType(Enum):
    square = 1
    round = 2

@dataclass
class Plate:
    id: int = 0
    name: str = 'Unknown'
    notes: str = ''
    width: float = 0.0
    length: float = 0.0
    num_rows: int = 0
    num_columns: int = 0
    num_wells: int = 0
    centre_first_well_offset_x: float = 0.0
    centre_first_well_offset_y: float = 0.0
    well_type: WellType = round
    well_dimension_x: float = 0.0
    well_dimension_y: float = 0.0
    well_spacing_x: float = 0.0
    well_spacing_y: float = 0.0
    min_well_volume: float = 0.0
    max_well_volume: float = 0.0

    def __post_init__(self):
        self.num_wells = self.num_columns * self.num_rows  # Calculate area after initialization

    

    
