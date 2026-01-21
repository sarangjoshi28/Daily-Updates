from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

students = []   

def load_students_from_api():
    global students

    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)

    if res.status_code == 200:
        api_data = res.json()
        students = []
        for i in api_data:
            students.append({
                "id": str(i["id"]),
                "name": i["name"],
                "age": 20  
            })
        print("Students loaded from API")
    else:
        print("Failed to fetch data from API")


@app.route("/students", methods=["GET"])
def get_all_students():
    return students

@app.route("/student", methods=["POST"])
def add_one_student():
    data = request.json

    if not data or "name" not in data or "age" not in data:
        return "incorrect data"

    new_id = str(len(students) + 1)

    new_student = {
        "id": new_id,
        "name": data["name"],
        "age": data["age"]
    }

    students.append(new_student)
    return  new_student

@app.route("/students/<id>", methods=["PUT"])
def update_student(id):
    data = request.json

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            return student

    return "student not found"

@app.route("/students/<id>", methods=["DELETE"])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return "student deleted"

    return "student not found"

if __name__ == "__main__":
    load_students_from_api()   
    app.run(port=4000, debug=True)


