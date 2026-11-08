from flask import Flask
from .extensions import appbuilder , db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    with app.app_context():
        appbuilder.init_app(app, db.session)
        from . import models
        from .models import Cliente, Membresia, Plan, Entrenador, Clase, Reserva
        from . import views

        #Registrar la view de la IA
        from .ai.asistente_ai import asistente_bp
        app.register_blueprint(asistente_bp);

        #Registrar la view de reportes
        from .reportes import reportes_bp
        app.register_blueprint(reportes_bp)
    return app

app = create_app()