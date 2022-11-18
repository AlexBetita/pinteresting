from .db import db, environment, SCHEMA


class Board(db.Model):

	'''

	relationships :
		boards <-- users
		boards --> pins
		boards <-> users collaborators

    '''

	__tablename__ = 'boards'

	if environment == "production":
		__table_args__ = {'schema': SCHEMA}

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	board_cover = db.Column(db.String)
	is_secret = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), ondelete='CASCADE')
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

	user = db.relationship('User', back_populates='boards', passive_deletes=True)
	pins = db.relationship('User', back_populates='board', cascade='all, delete-orphan')

	def to_dict(self):
		return {
			'id' : self.id,
			'name' : self.name,
			'board_cover' : self.board_cover,
			'is_secret' : self.is_secret,
			'user_id' : self.user_id,
			'created_on' : self.created_on,
			'updated_on' : self.updated_on
		}

	def to_dict_basic_info(self):
		return {
			'id' : self.id,
			'name' : self.name,
			'board_cover' : self.board_cover,
			'is_secret' : self.is_secret
		}
