# Consulta 05
#    5. 
#    5.1 En una consulta, obtener todos los cursos.
#    5.2 Realizar un ciclo repetitivo para obtener en cada iteración las entregas por cada curso (con otra consulta), 
#        y presentar el promedio de calificaciones de las entregas

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from clases import Curso, Tarea, Entrega
from config import cadena_base_datos

# Conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# 5.1 Obtener todos los cursos
cursos = session.query(Curso).all()

# 5.2 Por cada curso, obtener entregas de sus tareas y calcular el promedio
for curso in cursos:
    # Obtener IDs de tareas del curso actual
    tareas_ids = [t.id for t in curso.tareas]
    
    if tareas_ids:
        # Obtener promedio de calificaciones de todas las entregas de esas tareas
        promedio = session.query(func.avg(Entrega.calificacion)).filter(
            Entrega.tarea_id.in_(tareas_ids)
        ).scalar()
        
        promedio = round(promedio, 2) if promedio is not None else "Sin entregas"
    else:
        promedio = "Sin tareas"
    
    print(f"Curso: {curso.titulo} -> Promedio calificaciones: {promedio}")
