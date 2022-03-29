import json

from flask import request, Blueprint

from .models import Team, Events, League, db, Teamleague

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


@views.route('/join')
def join():
    # rows = db.session.query(Test.id, Test1.field1_1).join(Test1, Test.id == Test1.tid).order_by(Test.id).all()
    # rows = Events.join(League).select(Events.c.idevent == 467795).execute().first()
    # rows = Events.join(League, onclause=Events.c.idleague == League.c.idleague).\
    #     join(Team, onclause=Events.c.idhometeam == Team.c.idteam).\
    #     select().\
    #     execute().first()

    rows = League.join(Teamleague, League.c.idleague == Teamleague.c.idleague).\
        join(Team, Teamleague.c.idteam == Team.c.idteam).select().execute().all()

    print({'test': rows})
    return f'{rows}'


    # rows = Events.select(League.idleague, Events.strsport).join(Test1, League.idleague == Events.idleague)\
    #     .order_by(League.idleague).all()
    # jdata = []
    # for row in rows:
    #     jdata.append(row)


# with SessionContext() as session:
#     query = session.query(Test, Test1, Test2)
#     records = query.all()
#     for test, test1, test2 in records:
#         print(test, test1, test2)
