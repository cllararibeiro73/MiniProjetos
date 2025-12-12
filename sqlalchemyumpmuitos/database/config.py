from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Table, Column, String
from flask_login import UserMixin
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column,  relationship

# Criação do motor do banco de dados
engine = create_engine('sqlite:///database.db')

# Criando a sessão do banco de dados
session = Session(bind=engine)

# Definição da classe base
class Base(DeclarativeBase):
    pass

# Definindo a classe User (usuários)
class User(Base, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=False)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str] = mapped_column(unique=False)

    posts = relationship("Post", backref="autor")

class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column()
    conteudo: Mapped[str] = mapped_column()
    usuario_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  

def is_authenticated(self):
    return True  # O usuário está autenticado
    
def is_active(self):
    return True  # O usuário está ativo (mude conforme a lógica do seu sistema)

def is_anonymous(self):
    return False  # O usuário não é anônimo (nunca será em um sistema real)

def get_id(self):
    return str(self.id)  #


# Função para criar as tabelas no banco de dados
def start_db():
    Base.metadata.create_all(bind=engine)

def destroy_db():
    Base.metadata.drop_all(bind=engine)
