from sqlalchemy import Table, Column, ForeignKey, DateTime, Boolean
from database.config import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

class Consulta(Base):
    __tablename__ = 'consultas'

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    medico_id: Mapped[int] = mapped_column(ForeignKey('medicos.id'), nullable=False)
    paciente_id: Mapped[int] = mapped_column(ForeignKey('pacientes.id'), nullable=False)
    realizada: Mapped[bool] = mapped_column(Boolean, default=False) 
    
    medico = relationship('Medico', back_populates='consultas')
    paciente = relationship('Paciente', back_populates='consultas')