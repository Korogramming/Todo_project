from flask import Flask, render_template, redirect, request,url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>')



