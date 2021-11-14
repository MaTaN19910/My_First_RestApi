from flask import Flask, jsonify
app = Flask(__name__)

# database

courses = [{'name': "Malam", 'course_id': "0", 'Description': "Programming basic"},
           {'name': "OOP", 'course_id': "1", 'Description': "Advance Programming"}]


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




@app.route('/')
def hello():
    return 'Congratulations! you have successfully host Flask in a Docker container!'
if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug = True)


