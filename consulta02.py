# Obtener tTodos los departamentos que tengan notas de entregas menores o iguales a 0.3
# En función de los departamentos, presentar el nombre del departamento y el número de cursos que tiene cada departamento

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from clases import Departamento, Curso, Tarea, Entrega
from config import cadena_base_datos

# Conexión y sesion
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Subconsulta: IDs de departamentos que tienen entregas con nota <= 0.3
subconsulta = session.query(Departamento.id).join(Departamento.cursos).\
    join(Curso.tareas).join(Tarea.entregas).\
    filter(Entrega.calificacion <= 0.3).distinct()

# Consulta principal: departamentos filtrados y cantidad de cursos
resultados = session.query(
    Departamento.nombre,
    func.count(Curso.id).label("cantidad_cursos")
).join(Departamento.cursos).\
    filter(Departamento.id.in_(subconsulta)).\
    group_by(Departamento.id).all()

# Mostrar resultados
for depto in resultados:
    print(f"Departamento: {depto.nombre}, Cursos: {depto.cantidad_cursos}")
