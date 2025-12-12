from flask import Flask
from flask import render_template, redirect, url_for, request, flash
from flask_login import LoginManager
from flask_login import login_required, login_manager, login_user, logout_user, current_user
from database import session, User, start_db, Post

app = Flask(__name__)

start_db()

app.config['SECRET_KEY'] = 'dificil'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        user = User(nome=nome, email=email, senha=senha)
        session.add(user)
        session.commit()
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        user = session.query(User).filter(User.email == email).first()
        
        if user and user.senha == senha:
            login_user(user)
            return redirect(url_for('dash')) 
        else:
            flash('Credenciais inválidas, tente novamente.')
            return redirect(url_for('register')) 
        
    return render_template('login.html')

@app.route('/dash', methods=['POST', 'GET'])
@login_required
def dash():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        
        # Criar novo post
        post = Post(titulo=titulo, conteudo=conteudo, usuario_id=current_user.id)
        
        # Adicionar e salvar no banco de dados
        session.add(post)
        session.commit()
        return redirect(url_for('dash')) 
    usuario = session.query(User).filter(User.id == current_user.id).first()
    return render_template('dash.html', usuario=usuario)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
