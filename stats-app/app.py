from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Stats App is Running!", "status": "OK"})

@app.route('/stats')
def get_stats():
    try:
        response = requests.get('http://todo-app:5000/todos')
        todos = response.json()['todos']
        
        total = len(todos)
        completed = len([t for t in todos if t['completed']])
        
        return jsonify({
            "total_tasks": total,
            "completed": completed,
            "pending": total - completed,
            "completion_rate": f"{(completed/total*100):.1f}%" if total > 0 else "0%"
        })
    except Exception as e:
        return jsonify({"error": "Cannot connect to todo-app", "details": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
