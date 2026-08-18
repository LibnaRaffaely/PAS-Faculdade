from flask import render_template, request, redirect, url_for
from models.student import db

def index():
    """
    Controlador para a página inicial.
    Busca os dados no Model e os envia para a View.
    """
    students = db.get_all_students()
    return render_template('index.html', students=students)

def add_student():
    """
    Controlador para adicionar um novo aluno.
    Lida com a requisição (GET para mostrar o formulário, POST para salvar os dados).
    """
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        db.add_student(name, course)
        return redirect(url_for('index'))
    
    return render_template('add.html')
