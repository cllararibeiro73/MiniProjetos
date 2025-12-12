from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user
login_manager = LoginManager()
import sqlite3

database = 'database.db'

def obter_conexao():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

class User(UserMixin):
    def __init__(self,nome, email, senha,):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.usu_id = None

    @classmethod
    def get(cls, usu_id):
        conn = obter_conexao()
        SELECT = "SELECT * FROM usuario WHERE usu_id = ?"
        conn.execute(SELECT, (id,))
        dados = conn.fetchone()
        if dados:
            usuario = cls(dados['email'], dados['senha'])
            usuario.id = dados['usu_id']
            return usuario
        return None

    @classmethod
    def get_by_email(cls,email):
        conn = obter_conexao()
        user = conn.execute("SELECT usu_id, nome, email FROM usuario WHERE email = ?", (email,))
        dados = conn.fetchone()
        if dados:
            usuario =cls(dados['email'], dados['senha'])
            usuario.usu_id =dados['usu_id']
            return user
        return None
    
    def save(self):
        conn = obter_conexao()  
        cursor = conn.cursor()    
        cursor.execute("INSERT INTO usuario(nome, email, senha) VALUES (?,?,?)", (self.nome, self.email, self.senha))
        # salva o id no objeto recem salvo no banco
        conn.commit()
        conn.close()
        return True

@login_manager.user_loader
def load_user(usu_id):
    return User.get(usu_id)