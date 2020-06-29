from app import db


class Attendance(db.Model):
    __tablename__ = "attendance-table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.String(60), nullable=False)
    date = db.Column(db.Date, nullable=False)
    timestamp = db.Column(db.String(60))

    @staticmethod
    def get_attendance(date):
        return Attendance.query.filter_by(date=date).all()

