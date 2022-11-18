from .db import db, environment, SCHEMA
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .enum_values import countries, languages, pronouns

class User(db.Model, UserMixin):
	__tablename__ = 'users'

	if environment == "production":
		__table_args__ = {'schema': SCHEMA}

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), nullable=False, unique=True)
	hashed_password = db.Column(db.String(255), nullable=False)
	first_name = db.Column(db.String(40), nullable=False)
	last_name = db.Column(db.String(40))
	username = db.Column(db.String(40), nullable=False, unique=True)
	pronuns = db.Column(db.Enum(*pronouns))
	about = db.Column(db.String(500))
	website = db.Column(db.String(500))
	age = db.Column(db.Integer)
	profile_visits = db.Column(db.Integer)
	gender = db.Column(db.String(30))
	language = db.Column(db.Enum(*languages))
	country = db.Column(db.Enum(*countries))
	deactivated = db.Column(db.Boolean(), default=False)
	profile_pic = db.Column(db.String)
	finished_signup = db.Column(db.Boolean(), default=False)
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

	@property
	def password(self):
		return self.hashed_password

	@password.setter
	def password(self, password):
		self.hashed_password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	@staticmethod
	def set_default_first_name(email):
		return email[0].upper() + email.split('@')[0][1:]

	@staticmethod
	def set_default_username(email):
		return email.split('@')[0]

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'first_name': self.first_name,
			'last_name' : self.last_name,
			'username': self.username,
			'pronouns' : self.pronuns,
			'about' : self.about,
			'website' : self.website,
			'age' : self.age,
			'profile_visits' : self.profile_visits,
			'gender' : self.gender,
			'language' : self.language,
			'country' : self.country,
			'deactivated' : self.deactivated,
			'profile_pic' : self.profile_pic
        }

	def to_dict_signup(self):
		return {
			'id' : self.id,
			'first_name' : self.first_name,
			'username' : self.username,
			'email' : self.email,
			'age' : self.age,
		}
