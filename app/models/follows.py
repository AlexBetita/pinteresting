from .db import db, environment, SCHEMA


class Follow(db.Model):

	'''

	relationships :
		folower --> following --- users
		follows <-- messages
    '''

	__tablename__ = 'follows'

	if environment == "production":
		__table_args__ = {'schema': SCHEMA}

	id = db.Column(db.Integer, primary_key=True)
	follower_id = db.Column(db.Integer, db.ForeignKe('users.id'))
	following_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	is_following = db.Column(db.Boolean)
	unique_room_id = db.Column(db.Integer, unique=True)

	follower = db.relationship('User', foreign_keys=[follower_id], back_populates='followers')
	following = db.relationship('User', foreign_keys=[following_id], back_populates='followings')

	def to_dict(self):
		return {
			'id' : self.id,
			'follower_id' : self.follower_id,
			'following_id' : self.following_id,
			'is_following' : self.is_following,
			'unique_room_id' : self.unique_room_id
		}
