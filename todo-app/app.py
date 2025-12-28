from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Belajar Docker", "completed": False},
    {"id": 2, "task": "Buat laporan", "completed": True},
]

@app.route('/')
def home():
    return jsonify({"message": "Todo App is Running!", "status": "OK"})

@app.route('/todos')
def get_todos():
    return jsonify({"todos": todos, "total": len(todos)})

@app.route('/add/<task>')
def add_todo(task):
    new_id = max([t['id'] for t in todos]) + 1 if todos else 1
    new_todo = {"id": new_id, "task": task, "completed": False}
    todos.append(new_todo)
    return jsonify({"message": "Todo added", "todo": new_todo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
