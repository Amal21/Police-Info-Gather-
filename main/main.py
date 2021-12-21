from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Recherche(db.Model):
    id: int
    cin: str
    description: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    cin = db.Column(db.String(200))
    description = db.Column(db.String(200))


@dataclass
class RechercheUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    recherche_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'recherche_id', name='user_ recherche_unique')


@app.route('/api/recherches')
def index():
    return jsonify(Recherche.query.all())


@app.route('/api/recherches/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    #json = req.json()

    try:
        rechercheUser = RechercheUser(user_id=id, product_id=id)
        db.session.add(rechercheUser)
        db.session.commit()

        publish('recherche_liked', id)
    except:
        abort(400, 'You already liked ')

    return jsonify({'message':'success'})




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
