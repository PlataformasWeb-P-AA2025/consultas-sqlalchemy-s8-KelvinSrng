# Obtener las entregas de todos los estudiantes que pertenecen al departamento de Arte.
# Presentar: nombre de la tarea, nombre del estudiante, calificación, 
# nombre del instructor y nombre del departamento.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clases import Base, Entrega, Estudiante, Tarea, Curso, Instructor, Departamento
from config import cadena_base_datos

# Crear engine y sesion
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Realizamos la consulta con multiples joins
resultados = session.query(
    Tarea.titulo.label("nombre_tarea"),
    Estudiante.nombre.label("nombre_estudiante"),
    Entrega.calificacion,
    Instructor.nombre.label("nombre_instructor"),
    Departamento.nombre.label("nombre_departamento")
).join(
    Entrega.tarea
).join(
    Tarea.curso
).join(
    Curso.departamento
).join(
    Curso.instructor
).join(
    Entrega.estudiante
).filter(
    Departamento.nombre == "Arte"
).all()

# Mostrar resultados
for r in resultados:
    print(f"Tarea: {r.nombre_tarea}, Estudiante: {r.nombre_estudiante}, "
          f"Calificación: {r.calificacion}, Instructor: {r.nombre_instructor}, "
          f"Departamento: {r.nombre_departamento}")