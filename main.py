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
def edit_todo(todo_id):
    if 1 <= todo_id <= len(todos):
        return render_template('edit.html', todo=todos[todo_id-1], todo_id=todo_id)
    else:
        return redirect(url_for('index'))

@app.route('/update/<inr:todo_id>', methods=['POST'])
def update_todo(todo_id):
    if 1 <= todo_id <= len(todos):
        todo = request.form.get('todo')
        todos[todo_id-1] = todo
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    if 1 <= todo_id <= len(todos):
        del todos[todo_id-1]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

