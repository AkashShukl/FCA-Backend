from flask import request, jsonify
from app import app, db
from app.models import Attendance
from datetime import datetime


@app.route('/')
def test():
    """Serves functionality to test weather the server is working or not"""
    return {"res": "working"}


@app.route('/attendance', methods=["POST"])
def func():
    if request.method == "POST":
        content = request.get_json()
        print(content)
        temp = Attendance(
            name=content['name'],
            uid=content['uid'],
            date=content['date']
        )
        db.session.add(temp)
        db.session.commit()

        return {"ok": "success"}


@app.route('/getattendance', methods=["POST"])
def funct():
    if request.method == "POST":
        content = request.get_json()
        print("cont", content)
        results = Attendance.get_attendance(content["date"])
        item = []
        response = "heyp"
        for result in results:
            obj = {
                'uid': result.uid,
                'name': result.name,
                'date': result.date,
                'timestamp': datetime.now()
            }
            item.append(obj)
        response = jsonify(item)
        return response
