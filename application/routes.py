from application import app, db
from flask import render_template, request, redirect
from application.models import Todo

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return f"There was an issue adding your task"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)
    

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return f"There was an issue deleting that task"

        
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return f"There was an issue updating your task"
        
    else:
        return render_template('update.html', task=task)