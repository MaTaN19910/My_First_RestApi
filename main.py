from flask import Flask, jsonify

# this RestApi will run on flask
app = Flask(__name__)

# database

courses = [{'name': "Malam", 'course_id': "0", 'Description': "Programming basic"},
           {'name': "OOP", 'course_id': "1", 'Description': "Advance Programming"}]


@app.route('/')
def hello_world():
    return 'hello test'


# two get method

@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'Courses': courses[course_id]})


# post method
@app.route("/courses", methods=['POST'])
def create():
    course = {
        "Description": "Programming basic",
        "course_id": "2",
        "name": "Malam"
        ,
    }
    courses.append(course)
    return jsonify({'Created': course})

# method
@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({'course': courses[course_id]})


if __name__ == '__main__':
    app.run(debug=True)
