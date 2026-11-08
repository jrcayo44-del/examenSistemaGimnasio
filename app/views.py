from flask_appbuilder import BaseView, ModelView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Cliente, Membresia, Plan, Entrenador, Clase, Reserva
from . import appbuilder

class ClienteView(ModelView):
    datamodel = SQLAInterface(Cliente)
    label_columns = {
        "nombre": "Nombres",
        "apellido": "Apellidos",
        "carnet": "Carnet",
        "telefono": "Teléfono",
        "email": "Correo Electrónico",
        "fecha_registro": "Fecha de Registro"
    }
    list_columns = ["nombre", "apellido", "carnet", "telefono", "email", "fecha_registro"]
    show_columns = ["id_cliente", "nombre", "apellido", "carnet", "telefono", "email", "fecha_registro"]
    add_columns = ["nombre", "apellido", "carnet", "telefono", "email", "fecha_registro"]
    edit_columns = ["nombre", "apellido", "carnet", "telefono", "email"]
    order_columns = ["nombre"]

class MembresiaView(ModelView):
    datamodel = SQLAInterface(Membresia)
    label_columns = {
        "clientes": "Cliente",
        "planes": "Plan",
        "fecha_inicio": "Fecha de Inicio",
        "fecha_fin": "Fecha de Fin",
        "estado": "Estado"
    }

    list_columns = ["id_membresia", "clientes", "planes", "fecha_inicio", "fecha_fin", "estado"]
    show_columns = ["id_membresia", "clientes", "planes", "fecha_inicio", "fecha_fin", "estado"]
    add_columns = ["clientes", "planes", "fecha_inicio", "fecha_fin", "estado"]
    edit_columns = ["clientes", "planes", "fecha_inicio", "fecha_fin", "estado"]
    order_columns = ["fecha_inicio"]

class PlanView(ModelView):
    datamodel = SQLAInterface(Plan)
    label_columns = {
        "nombre_plan": "Plan",
        "descripcion": "Descripción",
        "duracion_meses": "Duración (meses)",
        "precio": "Precio"
    }

    list_columns = ["id_plan", "nombre_plan", "descripcion", "duracion_meses", "precio"]
    show_columns = ["id_plan", "nombre_plan", "descripcion", "duracion_meses", "precio"]
    add_columns = ["nombre_plan", "descripcion", "duracion_meses", "precio"]
    edit_columns = ["nombre_plan", "descripcion", "duracion_meses", "precio"]
    order_columns = ["nombre_plan"]

class EntrenadorView(ModelView):
    datamodel = SQLAInterface(Entrenador)
    label_columns = {
        "nombre": "Nombres",
        "apellido": "Apellidos",
        "especialidad": "Especialidad",
        "telefono": "Teléfono",
        "email": "Correo Electrónico"
    }

    list_columns = ["id_entrenador", "nombre", "apellido", "especialidad", "telefono", "email"]
    show_columns = ["id_entrenador", "nombre", "apellido", "especialidad", "telefono", "email"]
    add_columns = ["nombre", "apellido", "especialidad", "telefono", "email"]
    edit_columns = ["nombre", "apellido", "especialidad", "telefono", "email"]
    order_columns = ["nombre"]

class ClaseView(ModelView):
    datamodel = SQLAInterface(Clase)
    label_columns = {
        "nombre_clase": "Clase",
        "descripcion": "Descripción",
        "horario": "Horario",
        "entrenadores": "Entrenador"
    }

    list_columns = ["id_clase", "nombre_clase", "descripcion", "horario", "entrenadores"]
    show_columns = ["id_clase", "nombre_clase", "descripcion", "horario", "entrenadores"]
    add_columns = ["nombre_clase", "descripcion", "horario", "entrenadores"]
    edit_columns = ["nombre_clase", "descripcion", "horario", "entrenadores"]
    order_columns = ["nombre_clase"]

class ReservaView(ModelView):
    datamodel = SQLAInterface(Reserva)
    label_columns = {
        "clientes": "Cliente",
        "clases": "Clase",
        "fecha_reserva": "Fecha de Reserva",
        "estado": "Estado"
    }

    list_columns = ["id_reserva", "clientes", "clases", "fecha_reserva", "estado"]
    show_columns = ["id_reserva", "clientes",("clases"), "fecha_reserva", "estado"]
    add_columns = ["clientes",("clases"),"fecha_reserva",("estado")]
    edit_columns = ["clientes",("clases"),"fecha_reserva",("estado")]
    order_columns = ["fecha_reserva"]

# Registro de las vistas en Flask AppBuilder
appbuilder.add_view(
    ClienteView,
    "Clientes",
    icon="fa-users",
    category="Clientes"
)
appbuilder.add_view(
    MembresiaView,
    "Membresías",
    icon="fa-id-card",
    category="Membresías"
)
appbuilder.add_view(
    PlanView,
    "Planes",
    icon="fa-list",
    category="Planes"
)
appbuilder.add_view(
    EntrenadorView,
    "Entrenadores",
    icon="fa-user-tie",
    category="Entrenadores"
)
appbuilder.add_view(
    ClaseView,
    "Clases",
    icon="fa-chalkboard-teacher",
    category="Clases"
)
appbuilder.add_view(
    ReservaView,
    "Reservas",
    icon="fa-calendar-check",
    category="Reservas"
)

class DashboardView(BaseView):
    route_base = "/dashboard"
    default_view = 'index'

    @expose('/')
    def index(self):
        return self.render_template('dashboard.html')

appbuilder.add_view(
    DashboardView,
    "Dashboard",
    icon="fa-dashboard",
    category="Menu principal"
)