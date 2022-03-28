from . import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.VARCHAR())
    field2 = db.Column(db.VARCHAR())

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    class Meta:
        managed = False
        db_table = 'test'
