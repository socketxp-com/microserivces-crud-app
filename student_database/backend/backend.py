import psycopg2
import flask
from flask import request, jsonify

from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

admissionNum = 1000

con = psycopg2.connect(database="postgres", user="gannygans", password="cisco123", host="postgres", port="5432")
print("Database opened successfully")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS STUDENT;")
con.commit()

cur.execute('''CREATE TABLE STUDENT
      (ADMISSION INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      COURSE        CHAR(50));''')
print("Table created successfully")

con.commit()


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/students', methods=['GET'])
@cross_origin()
def api_get_all_students():
    query = "SELECT * FROM STUDENT"
    cur.execute(query)
    print(cur.description)
    #fields = map(lambda x:x[0], cur.description)
    #print(fields)
    #result = [dict(zip(fields,row))   for row in cur.fetchall()]
    result = cur.fetchall()
    return jsonify(result)

@app.route('/api/v1/students', methods=['POST'])
def api_add_student():
    query_parameters = request.args

    name = query_parameters.get('name')
    age = query_parameters.get('age')
    course = query_parameters.get('course')

    print(name, age, course)
    global admissionNum

    query = "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE) VALUES (" + str(admissionNum) + ",'" + name + "', " + str(age) + ",'" + course + "'" + ")"

    admissionNum = admissionNum + 1
    cur.execute(query)
    con.commit()
    return jsonify(None)

@app.route('/api/v1/students', methods=['DELETE'])
def api_del_student():
    query_parameters = request.args
    admNum = query_parameters.get('admission')

    query = "DELETE FROM STUDENT WHERE ADMISSION=" + str(admNum)
    cur.execute(query)
    con.commit()
    return jsonify(None)
 
app.run()
con.close()
