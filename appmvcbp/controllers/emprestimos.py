from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.user import User
from models.book import Book
from models.emprestimo import Emprestimo

bp = Blueprint('emprestimos', __name__, url_prefix='/emprestimos')

#@bp.route('/')
#def index():
    #return render_template('books/index.html', books = Book.all())

@bp.route('/emprestimos', methods=['POST', 'GET'])
def emprestimos():
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']

        emprestimo = Emprestimo(titulo, user)
        emprestimo.save()
        return redirect(url_for('emprestimos.realizados'))

    return render_template('emprestimos/emprestimos.html', users=User.all())

@bp.route('/realizados', methods=['POST', 'GET'])
def realizados():
    livros_emprestados = Emprestimo.all()
    return render_template('emprestimos/realizados.html', livros=livros_emprestados)