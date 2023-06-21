from dataclasses import dataclass

@dataclass
class PersonaDTO:
        id: int
        fecha_nacimiento: str
        genero: str
        codigo_postal: str
        nombre: str