from sqlalchemy import create_engine, MetaData, Table

from . import db

engine = create_engine('postgresql://dnv:dnv@localhost/dbsporttest', convert_unicode=True)
metadata = MetaData(bind=engine)

Events = Table('events', metadata, autoload=True)
League = Table('league', metadata, autoload=True)
Team = Table('team', metadata, autoload=True)
TeamLeague = Table('teamleague', metadata, autoload=True)


# class Test(db.Model):
#     __tablename__ = 'test'
#     id = db.Column(db.Integer(), primary_key=True)
#     field1 = db.Column(db.VARCHAR())
#     field2 = db.Column(db.VARCHAR())
#
#     def __init__(self, field1, field2):
#         self.field1 = field1
#         self.field2 = field2
#
#     class Meta:
#         managed = False
#
#
# class Test1(db.Model):
#     __tablename__ = 'test1'
#     id = db.Column(db.Integer(), primary_key=True)
#     tid = db.Column(db.Integer(), ForeignKey('test.id'))
#     field1_1 = db.Column(db.VARCHAR())
#     field2_1 = db.Column(db.VARCHAR())
#
#     def __init__(self, field1_1, field2_1):
#         self.field1 = field1_1
#         self.field2 = field2_1
#
#
# class Test2(db.Model):
#     __tablename__ = 'test2'
#     id = db.Column(db.Integer(), primary_key=True)
#     t2id = db.Column(db.Integer(), ForeignKey('test1.id'))
#     field1_2 = db.Column(db.VARCHAR())
#     field2_2 = db.Column(db.VARCHAR())
#
#     def __init__(self, field1_2, field2_2):
#         self.field1 = field1_2
#         self.field2 = field2_2


# class Events(db.Model):
#     __tablename__ = 'events'
#
#     class Meta:
#         managed = False
#
#
# class League(db.Model):
#     __tablename__ = 'league'
#
#     class Meta:
#         managed = False
