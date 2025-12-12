from flask import Flask, render_template, request, redirect, url_for, flash
from database.config import Session, engine, Base
from models import Medico, Paciente, Consulta
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'dificil'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = session.query(Medico).get(int(user_id)) 
    if user is None:
        user = session.query(Paciente).get(int(user_id))
    return user


session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        role = request.form['role']

        if role == 'medico':
            medico = session.query(Medico).filter_by(email=email).first()

            if medico and check_password_hash(medico.senha, senha):
                login_user(medico)
                return redirect(url_for('medicodash'))

        elif role == 'paciente':
            paciente = session.query(Paciente).filter_by(email=email).first()
            if paciente and check_password_hash(paciente.senha, senha):
                login_user(paciente)
                return redirect(url_for('pacientedash'))    

    return render_template('login.html')

@app.route('/cadmedico', methods=['GET', 'POST'])
def cadmedico():
    if request.method == 'POST':
        nome = request.form['nome']
        especialidade = request.form['especialidade']
        email = request.form['email']
        senha = request.form['senha']

        medico = Medico(nome=nome, especialidade=especialidade, email=email)
        medico.set_password(senha)
        session.add(medico)
        session.commit()
        return redirect(url_for('login'))

    return render_template('cadmedico.html')

@app.route('/cadpaciente', methods=['GET', 'POST'])
def cadpaciente():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        paciente = Paciente(nome=nome, email=email)
        paciente.set_password(senha)
        session.add(paciente)
        session.commit()
        return redirect(url_for('login'))

    return render_template('cadpaciente.html')   

@app.route('/medicodash',methods=['GET', 'POST'])
@login_required
def medicodash():
    consultas_realizadas = session.query(Consulta).filter_by(medico_id=current_user.id, realizada=True).all()
    consultas_agendadas = session.query(Consulta).filter_by(medico_id=current_user.id, realizada=False).all()
    pacientes = session.query(Paciente).all()

    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        data = request.form['data']
        realizada = 'realizada' in request.form  
        nova_consulta = Consulta(medico_id=current_user.id, paciente_id=paciente_id,data=datetime.strptime(data, '%Y-%m-%dT%H:%M'),
        realizada=realizada)
        session.add(nova_consulta)
        session.commit()
        return redirect(url_for('medicodash'))

    return render_template('dashmedico.html', medico=current_user, consultas_realizadas=consultas_realizadas,
    consultas_agendadas=consultas_agendadas,pacientes=pacientes)

@app.route('/pacientedash',methods=['GET', 'POST'])
@login_required
def pacientedash():
    consultas_realizadas = session.query(Consulta).filter_by(paciente_id=current_user.id, realizada=True).all()
    consultas_agendadas = session.query(Consulta).filter_by(paciente_id=current_user.id, realizada=False).all()
    return render_template('dashpaciente.html', paciente=current_user, consultas_realizadas=consultas_realizadas,
    consultas_agendadas=consultas_agendadas)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



