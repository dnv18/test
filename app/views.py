import json

import flask_restless
from flask import request, Blueprint, jsonify
from sqlalchemy import select

from .models import Team, Events, League, db, TeamLeague, fs_mixin, Test, engine

views = Blueprint('views', __name__)
#
# @views.route('/app', methods=['POST', 'GET'])
# def test_getpost():
#     if request.method == 'POST':
#         if request.is_json:
#             data = request.get_json()
#             new_data = Test(field1=data['field1'], field2=data['field2'])
#             db.session.add(new_data)
#             db.session.commit()
#             return {'message': 'New row was created'}
#         else:
#             return {'message': 'Error'}
#     elif request.method == 'GET':
#         rows = Test.query.all()
#         results = [
#             {
#                 'id': row.id,
#                 'field1': row.field1,
#                 'field2': row.field2
#             } for row in rows]
#         return {'count': len(results), 'rows': results}
#
#
# @views.route('/app/<id>', methods=['GET', 'PUT', 'DELETE'])
# def test_rud(id):
#     row = Test.query.get_or_404(id)
#
#     if request.method == 'GET':
#         response = {
#             'id': row.id,
#             'field1': row.field1,
#             'field2': row.field2
#         }
#         return response
#     elif request.method == 'PUT':
#         data = request.get_json()
#         row.field1 = data['field1']
#         row.field2 = data['field2']
#         db.session.add(row)
#         db.session.commit()
#         return {'message': 'Updated'}
#     elif request.method == 'DELETE':
#         db.session.delete(row)
#         db.session.commit()
#         return {'message': 'Deleted'}


@views.route('/join', methods=['GET'])
def join():
    # rows = db.session.query(Test.id, Test1.field1_1).join(Test1, Test.id == Test1.tid).order_by(Test.id).all()
    # rows = Events.outerjoin(League).select(Events.c.idevent == 467795).execute().first()
    # rows = Events.select(Events.c.idevent >= 1).execute().first()
    rows = League.select().execute()
    row = rows.fetchone()
    print(row[League.c.idleague], row[1])

    # rows = Events.join(League, onclause=Events.c.idleague == League.c.idleague). \
    #     join(Team, onclause=Events.c.idhometeam == Team.c.idteam). \
    #     select().\
    #     execute()
    data = []
    for row in rows:
        d = dict(row.items())
        data.append(d)
    # return '1'
    return jsonify({League.name: data[:10]})


    # rows = League.join(TeamLeague, League.c.idleague == TeamLeague.c.idleague).\
    #     join(Team, TeamLeague.c.idteam == Team.c.idteam).select().execute().first()

    # rows = engine.execute('select * from Test where id = 1').all()
    # print({'test': rows})
    # rows = Test.query.all()
    # fs_mixin.fs_json_list(rows)
    # return fs_mixin.fs_get_delete_put_post(rows)

    # return {'test': data}

    # rows = Events.select(League.idleague, Events.strsport).join(Test1, League.idleague == Events.idleague)\
    #     .order_by(League.idleague).all()
    # jdata = []
    # for row in rows:
    #     jdata.append(row)



