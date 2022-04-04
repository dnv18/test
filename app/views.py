from flask import Blueprint, jsonify
from sqlalchemy import select

from .models import Team, Events, League, TeamLeague, Test1

views = Blueprint('views', __name__)


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


# @views.route('/join', methods=['GET'])
# def join():
#     data = []
#     rows = (select([League.c.strleague, Team.c.strteam])
#             .select_from(League.join(TeamLeague, onclause=League.c.idleague == TeamLeague.c.idleague)
#                          .join(Team, onclause=TeamLeague.c.idteam == Team.c.idteam))).execute()
#     for row in rows:
#         d = dict(row.items())
#         data.append(d)
#     return jsonify({'TeamsByLeague': data})


@views.route('/leagues', methods=['GET'])
def get_leagues():
    data = []
    leagues = League.select().order_by(League.c.idleague).execute()

    for league in leagues:
        d_league = dict(league.items())
        teams = Team.select()\
            .join(TeamLeague, onclause=Team.c.idteam == TeamLeague.c.idteam)\
            .where(league.idleague == TeamLeague.c.idleague).execute()
        d_teams_in_league = []
        for team in teams:
            d_teams_in_league.append(dict(team.items()))
        d_league['Teamsset'] = d_teams_in_league
        data.append(d_league)

    # return jsonify({'Leagues': data[:5]})
    return jsonify(data[:5])
