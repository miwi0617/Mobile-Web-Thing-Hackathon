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
    name = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(512), unique=False)
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
        return '[name: %r, description:%r, thumbmnail:%r, model:%r, download: '
                '%r]' % (self.name, self.description, self.thumbmnail,
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
        return 'No brah, you cannot go there'

#     if name and description:
#         results = db.session.query(User).filter(User.name.like(name)).filter(User.description.like(description)).all()
#     elif name:
#         results = db.session.query(User).filter(User.name.like(name)).all()
#     elif description:
#         results = db.session.query(User).filter(User.description.like(description)).all()

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

