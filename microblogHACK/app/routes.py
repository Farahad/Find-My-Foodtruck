from flask import render_template, flash, redirect, url_for, request

from app import app, db
from app.models import User

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/BrinkleyD./Development/microblogHACK/app.db'
# db = SQLAlchemy(app)

class User():
    id = db.Column(db.Integer, primary_key=True)
    fTName = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(254))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self,fTName,description,latitude,longitude):
        self.fTName = fTName
        self.description = description
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<User %r>' % self.fTName

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['fTName'], request.form['description'], request.form['latitude'], request.form['longitude'])
    db.session.add(user)
    db.session.commit()

    return render_template('index.html', title='Home')



if __name__ == '__main__':
    app.run()
