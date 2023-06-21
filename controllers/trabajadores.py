from personas import Personas
class Trabajadores(Personas):

    def __init__(self, nombre, fecha_nacimiento, genero, codigo_postal, fecha_alta, puesto, horario_trabajo, categoria, id = None):
        super().__init__(nombre, fecha_nacimiento, genero, codigo_postal, id)
        self.fecha_alta = fecha_alta
        self.puesto = puesto
        self.horario_trabajo = horario_trabajo
        self.categoria = categoria
        
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
    nombre = 'Lucas Martinez',
    genero='H',
    categoria='C',
    puesto='Ingeniero',
    horario_trabajo='09.00-18.00hs',
    id=1254,
    codigo_postal='B1713'
)
print(t)
