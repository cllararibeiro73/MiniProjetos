from sqlalchemy import Table, Column, ForeignKey, DateTime
from database.config import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Medico(Base, UserMixin):
    __tablename__ = 'medicos'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    especialidade: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    consultas: Mapped[List['Consulta']] = relationship('Consulta', back_populates='medico')
    pacientes: Mapped[List['Paciente']] = relationship('Paciente', secondary='consultas',
    back_populates='medicos')

    def set_password(self, password: str):
        self.senha = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.senha, password)

    def get_id(self):
        return str(self.id)

