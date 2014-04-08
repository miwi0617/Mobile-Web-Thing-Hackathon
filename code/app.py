from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///week12.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), unique=False)
    description = db.Column(db.String(1024), unique=False)
    thumbmnail = db.Column(db.String(1024), unique=False)
    model = db.Column(db.String(1024), unique=False)
    download = db.Column(db.String(1024), unique=False)

    def __init__(self, name, description, thumbmnail, model, download):
        self.name = name
        self.description = description
        self.thumbmnail = thumbmnail
        self.model = model
        self.download = download

    def __repr__(self):
        return ('[name: %r, description:%r, thumbmnail:%r, model:%r, download:'
                ' %r]') % (self.name, self.description, self.thumbmnail,
                           self.model, self.download)


@app.route('/view/')

@app.route('/view/<name>')
def view(name=None):

    name = User.query.filter_by(name=name).first()

    return render_template('view.html', name=name)



@app.route('/search', methods=['GET'])
def search():
    try:
        name = request.args.get('name', '')
        description = request.args.get('description', '')
    except KeyError:
        return 'Could not find anything'

    if name and description:
        results = db.session.query(User).filter(User.name.like(name)).filter(User.description.like(description)).all()
    elif name:
        results = db.session.query(User).filter(User.name.like(name)).all()
    elif description:
        results = db.session.query(User).filter(User.description.like(description)).all()

    return render_template('search.html', results=results)

if __name__ == "__main__":
    app.run()

h = [User('Chair', 'The most amazing chair you will find in the world', 'Furniture/Chair_pic.png', 'Furniture/Chair.scad', 'DOWNLOAD'),
User('Stool', 'One of the most amazing stools you will find in the world','Furniture/Stool_pic.png', 'Furniture/Stool1.scad', 'DOWNLOAD'),
User('Bench', 'This is an awesome bench','bench.JPG', 'bench.scad', 'DOWNLOAD')]

