from database import get_connection
from models.book import Book
class Emprestimo:
    def __init__(self, emp_book, emp_user):
        self.emp_book = emp_book
        self.emp_user = emp_user

    def save(self):
        # Verifica se o livro existe antes de realizar o empréstimo
        if Book.exists(self.emp_book):
            conn = get_connection()
            conn.execute("INSERT INTO emprestimos(emp_book, emp_user) VALUES(?, ?)", (self.emp_book, self.emp_user))
            conn.commit()
            conn.close()
            return True
        else:
            return False  # Retorna False se o livro não existir

    @classmethod
    def select(cls):
        conn = get_connection()
        book = conn.execute("SELECT * FROM books").fetchall()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        emprestados = conn.execute("SELECT * FROM emprestimos ").fetchall()
        return emprestados


#DEU ERRADO 
    @classmethod
    def get_livros_emprestados(cls):
        conn = get_connection()
        query = """
        SELECT emprestimos.emp_user, books.titulo 
        FROM emprestimos 
        JOIN books ON emprestimos.emp_book = books.id
        """
        livros_emprestados = conn.execute(query).fetchall()
        conn.close()
        return livros_emprestados