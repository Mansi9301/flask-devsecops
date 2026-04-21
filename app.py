from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Buy groceries", "done": False},
    {"id": 2, "task": "Read a book", "done": False},
]

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos), 200

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo), 200

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400
    new_todo = {
        "id": len(todos) + 1,
        "task": data["task"],
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    todos.remove(todo)
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)