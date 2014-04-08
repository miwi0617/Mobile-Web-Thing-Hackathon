from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80), unique=False)
    capacity = db.Column(db.String(80), unique=False)
    contact = db.Column(db.String(80), unique=False)
    image_url = db.Column(db.String(1024), unique=False)

    def __init__(self, location, capacity, contact, image_url):
        self.location = location
        self.capacity = capacity
        self.contact = contact
        self.image_url = image_url

    def __repr__(self):
        return '[location: %r, capacity:%r, contact:%r, URL:%r]' % (
            self.location, self.capacity, self.contact, self.image_url)


@app.route('/view/')

@app.route('/view/<name>')
def view(name=None):

    location = User.query.filter_by(location=name).first()

    return render_template('view.html', location=location)



@app.route('/search', methods=['GET'])
def search():
    try:
        location = request.args.get('location', '')
        capacity = request.args.get('capacity', '')
    except KeyError:
        return 'No brah, you cannot go there'

    if location and capacity:
        results = db.session.query(User).filter(User.location.like(location)).filter(User.capacity.like(capacity)).all()
    elif location:
        results = db.session.query(User).filter(User.location.like(location)).all()
    elif capacity:
        results = db.session.query(User).filter(User.capacity.like(capacity)).all()    
    # results = db.session.query(User).filter(User.location.like(location)).filter(User.capacity.like(capacity)).all()
    #results += db.session.query(User).filter(User.capacity.like(capacity)).all()

    return render_template('search.html', results=results)

if __name__ == "__main__":
    app.run()

h = [User('Boulder', '5', '303.555.8787', 'http://i.imgur.com/ixqX0UO.png'),
User('Longmont', '2', '798.484.8584', 'http://i.imgur.com/uqGLZ2u.png'),
User('Boulder', '3', '784.451.8482', 'http://i.imgur.com/jdPZy2Y.png'),
User('Superior', '3', '989.565.2323', 'http://i.imgur.com/oFUs9Fm.png'),
User('Denver', '4', '415.635.5487', 'http://i.imgur.com/vuWeLzw.png'),
User('Longmont', '2', '784.562.3652', 'http://i.imgur.com/KbVHApe.png'),
User('Devner', '1', '452.365.2858', 'http://i.imgur.com/KbVHApe.png'),
User('Boulder', '4', '415.212.3524', 'http://i.imgur.com/p0Jf7UI.png'),
User('Superior', '5', '452.365.5214', 'http://i.imgur.com/fFkXPVN.png'),
User('Denver', '2', '254.236.9856', 'http://i.imgur.com/QtcbHtV.png'),
User('Boulder', '3', '121.555.5685', 'http://i.imgur.com/bI9prTC.png')]

