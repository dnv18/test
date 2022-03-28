from flask import request, Blueprint


from .models import Test, db

views = Blueprint('views', __name__)


@views.route('/app', methods=['POST', 'GET'])
def test_getpost():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_data = Test(field1=data['field1'], field2=data['field2'])
            db.session.add(new_data)
            db.session.commit()
            return {'message': 'New row was created'}
        else:
            return {'message': 'Error'}
    elif request.method == 'GET':
        rows = Test.query.all()
        results = [
            {
                'id': row.id,
                'field1': row.field1,
                'field2': row.field2
            } for row in rows]
        return {'count': len(results), 'rows': results}


@views.route('/app/<id>', methods=['GET', 'PUT', 'DELETE'])
def test_rud(id):
    row = Test.query.get_or_404(id)

    if request.method == 'GET':
        response = {
            'id': row.id,
            'field1': row.field1,
            'field2': row.field2
        }
        return response
    elif request.method == 'PUT':
        data = request.get_json()
        row.field1 = data['field1']
        row.field2 = data['field2']
        db.session.add(row)
        db.session.commit()
        return {'message': 'Updated'}
    elif request.method == 'DELETE':
        db.session.delete(row)
        db.session.commit()
        return {'message': 'Deleted'}