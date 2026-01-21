from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

students = []   


def load_students_from_fake_api():
    global students

    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)

    if res.status_code == 200:
        api_data = res.json()
        students = []
        for u in api_data:
            students.append({
                "id": str(u["id"]),
                "name": u["name"],
                "age": 20  
            })
        print("Students loaded from fake API")
    else:
        print("Failed to fetch data from fake API")

@app.route("/student/<id>", methods=["GET"])
def get_one_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({"message": "No student found with given Id"}), 404

@app.route("/student", methods=["POST"])
def add_one_student():
    data = request.json

    if not data or "name" not in data or "age" not in data:
        return jsonify({"message": "Send proper data {name, age}"}), 400

    new_id = str(len(students) + 1)

    new_student = {
        "id": new_id,
        "name": data["name"],
        "age": data["age"]
    }

    students.append(new_student)
    return jsonify(new_student), 201

@app.route("/students/<id>", methods=["PUT"])
def update_one_student(id):
    data = request.json

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

@app.route("/students/<id>", methods=["DELETE"])
def delete_one_student(id):
    for index, student in enumerate(students):
        if student["id"] == id:
            students.pop(index)
            return jsonify({"message": "Student deleted"})

    return jsonify({"message": "Student not found"}), 404


if __name__ == "__main__":
    load_students_from_fake_api()   
    app.run(port=4000, debug=True)


