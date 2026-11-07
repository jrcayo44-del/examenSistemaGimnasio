from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Cliente(Model):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    apellido = Column(String(100), unique=True, nullable=False)
    carnet = Column(String(20), unique=True, nullable=False)
    telefono = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    fecha_registro = Column(Date, nullable=False)

    membresias = relationship("Membresia", back_populates="clientes")
    reservas = relationship("Reserva", back_populates="clientes")

    def __repr__(self):
        return f"{self.nombre} {self.apellido}"

class Membresia(Model):
    __tablename__ = "membresias"

    id_membresia = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    id_plan = Column(Integer, ForeignKey("planes.id_plan"), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    estado = Column(Boolean, default=True, nullable=False)

    clientes = relationship("Cliente", back_populates="membresias")
    planes = relationship("Plan", back_populates="membresias")
    def __repr__(self):
        return f"Membresia {self.id_membresia} - Cliente {self.clientes.nombre} {self.clientes.apellido} - Plan {self.planes.nombre_plan} - Estado: {'Activa' if self.estado else 'Inactiva'}"

class Plan(Model):
    __tablename__ = "planes"

    id_plan = Column(Integer, primary_key=True)
    nombre_plan = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)
    duracion_meses = Column(Integer, nullable=False)
    precio = Column(Numeric(12, 2), nullable=False)

    membresias = relationship("Membresia", back_populates="planes")

    def __repr__(self):
        return f"{self.nombre_plan} - {self.descripcion} - Precio: {self.precio}"

class Entrenador(Model):
    __tablename__ = "entrenadores"

    id_entrenador = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    apellido = Column(String(100), unique=True, nullable=False)
    especialidad = Column(String(100), nullable=False)
    telefono = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    clases = relationship("Clase", back_populates="entrenadores")

    def __repr__(self):
        return f"{self.nombre} {self.apellido} - Especialidad: {self.especialidad}"

class Clase(Model):
    __tablename__ = "clases"

    id_clase = Column(Integer, primary_key=True)
    id_entrenador = Column(Integer, ForeignKey("entrenadores.id_entrenador"), nullable=False)
    nombre_clase = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)
    horario = Column(String(50), nullable=False)

    entrenadores = relationship("Entrenador", back_populates="clases")
    reservas = relationship("Reserva", back_populates="clases")

    def __repr__(self):
        return f"{self.nombre_clase} - {self.descripcion} - Horario: {self.horario} - Entrenador: {self.entrenador.nombre} {self.entrenador.apellido}"

class Reserva(Model):
    __tablename__ = "reservas"

    id_reserva = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    id_clase = Column(Integer, ForeignKey("clases.id_clase"), nullable=False)
    fecha_reserva = Column(Date, nullable=False)
    estado = Column(Boolean, default=True, nullable=False)

    clientes = relationship("Cliente", back_populates="reservas")
    clases = relationship("Clase", back_populates="reservas")

    def __repr__(self):
        return f"Reserva {self.id_reserva} - Cliente {self.clientes.nombre} {self.clientes.apellido} - Clase {self.clases.nombre_clase} - Fecha: {self.fecha_reserva}"
