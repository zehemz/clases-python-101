from flask import Flask
#from sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique= True)
	email = db.Column(db.String(255), unique=True)
   
	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' %self.username


@app.route('/')
def index():
	return "<h1 style='color:red'>Hello Flask</h1>"

if __name__ == "__main__":
	app.run()
