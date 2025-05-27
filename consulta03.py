# Obtener todas las tareas asignadas a los siguientes estudiantes 
#    Jennifer Bolton 
#    Elaine Perez
#    Heather Henderson
#    Charles Harris
#    En función de cada tarea, presentar el número de entregas que tiene

from sqlalchemy import create_engine, func, or_
from sqlalchemy.orm import sessionmaker
from clases import Estudiante, Entrega, Tarea
from config import cadena_base_datos

# Conexión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta con OR para obtener tareas entregadas por los estudiantes indicados
tareas_ids = session.query(Entrega.tarea_id).join(Entrega.estudiante).filter(
    or_(
        Estudiante.nombre == "Jennifer Bolton",
        Estudiante.nombre == "Elaine Perez",
        Estudiante.nombre == "Heather Henderson",
        Estudiante.nombre == "Charles Harris"
    )
).distinct()

# Consulta para contar entregas por cada tarea
resultados = session.query(
    Tarea.titulo,
    func.count(Entrega.id).label("numero_entregas")
).join(Entrega).\
    filter(Tarea.id.in_(tareas_ids)).\
    group_by(Tarea.id).all()

# Mostrar resultados
for r in resultados:
    print(f"Tarea: {r.titulo}, Número de entregas: {r.numero_entregas}")
