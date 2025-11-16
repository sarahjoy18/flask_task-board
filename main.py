from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Store todos and team members in JSON files
TODOS_FILE = 'todos.json'
TEAM_FILE = 'team_members.json'

def load_todos():
    if os.path.exists(TODOS_FILE):
        with open(TODOS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODOS_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def load_team():
    if os.path.exists(TEAM_FILE):
        with open(TEAM_FILE, 'r') as f:
            return json.load(f)
    return []

def save_team(team):
    with open(TEAM_FILE, 'w') as f:
        json.dump(team, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(load_todos())

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json
    todos = load_todos()
    new_todo = {
        'id': len(todos) + 1,
        'title': data.get('title'),
        'status': 'todo',
        'assignees': data.get('assignees', [])
    }
    todos.append(new_todo)
    save_todos(todos)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['status'] = data.get('status', todo['status'])
            todo['title'] = data.get('title', todo['title'])
            todo['assignees'] = data.get('assignees', todo.get('assignees', []))
            save_todos(todos)
            return jsonify(todo)
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)
    return '', 204

@app.route('/api/team', methods=['GET'])
def get_team():
    return jsonify(load_team())

@app.route('/api/team', methods=['POST'])
def add_team_member():
    data = request.json
    team = load_team()
    new_member = {
        'id': len(team) + 1,
        'name': data.get('name'),
        'color': data.get('color', '#667eea')
    }
    team.append(new_member)
    save_team(team)
    return jsonify(new_member), 201

@app.route('/api/team/<int:member_id>', methods=['DELETE'])
def delete_team_member(member_id):
    team = load_team()
    team = [member for member in team if member['id'] != member_id]
    save_team(team)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    app.run(debug=True, port=5000)