from app import app, db
from app.models import Cliente, Membresia, Plan, Entrenador, Clase, Reserva

with app.app_context():
    metadata = Cliente.metadata
    metadata = Membresia.metadata
    metadata = Plan.metadata
    metadata = Entrenador.metadata
    metadata = Clase.metadata
    metadata = Reserva.metadata
    
    engine = db.engine
    for tabla in metadata.sorted_tables:
        print("--", tabla.name)

    metadata.create_all(bind=engine)
    print("Creado correctamente")