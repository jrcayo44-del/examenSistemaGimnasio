from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func

from .extensions import db
from .models import Cliente, Membresia, Entrenador, Clase, Plan, Reserva


reportes_bp = Blueprint("reportes", __name__)

# REPORTE 1: CLIENTES REGISTRADOS

@reportes_bp.route("/reportes/cliente")
@login_required
def reporte_cliente():
    total_clientes = db.session.query(func.count(Cliente.id_cliente)).scalar()

    total_membresias = db.session.query(func.count(Membresia.id_membresia)).scalar()

    total_entrenadores = db.session.query(func.count(Entrenador.id_entrenador)).scalar()

    total_clases = db.session.query(func.count(Clase.id_clase)).scalar()

    total_planes = db.session.query(func.count(Plan.id_plan)).scalar()

    total_reservas = db.session.query(func.count(Reserva.id_reserva)).scalar()

    return render_template("reportes.html", 
                           total_clientes=total_clientes, 
                           total_membresias=total_membresias, 
                           total_entrenadores=total_entrenadores, 
                           total_clases=total_clases, 
                           total_planes=total_planes, 
                           total_reservas=total_reservas)


