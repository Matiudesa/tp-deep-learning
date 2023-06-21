from controllers.personas import Personas
from dtos.trabajadoresDTO import TrabajadoresDTO

class Trabajadores(Personas, TrabajadoresDTO):

    def __repr__(self):
        base_repr = super().__repr__()
        trabajadores_repr = list()
        trabajadores_repr.append(f'Fecha_alta: {self.fecha_alta}')
        trabajadores_repr.append(f'Puesto: {self.puesto}')
        trabajadores_repr.append(f'Horario de trabajo: {self.horario_trabajo}')
        trabajadores_repr.append(f'Categoria: {self.categoria}')
        return base_repr + "\n" + "\n".join(trabajadores_repr)


t = Trabajadores(
    fecha_alta= '15/05/2005',
    fecha_nacimiento= '11/04/2000',
    nombre='Lucas Martinez',
    genero='M',
    categoria='C',
    puesto='Vendedor',
    horario_trabajo='09.00-18.00hs',
    id=1254,
    codigo_postal='B1713'
)
print(t)
