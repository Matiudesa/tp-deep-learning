from dataclasses import dataclass
from dtos.personasDTO import PersonaDTO

@dataclass
class TrabajadoresDTO(PersonaDTO):
    fecha_alta: str
    puesto: str
    categoria: str
    horario_trabajo: str

