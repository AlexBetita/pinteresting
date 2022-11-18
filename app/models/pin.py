from .db import db, environment, SCHEMA


class Pin(db.Model):

	'''

    impressions should be incremented each time a pin is
	returned in a request

	relationships :
		pins <-- boards
		pins <-> topics --- pins_topic
		pins <-> users --- saved_pins
		pins <-- comments
    '''
	__tablename__ = 'pins'

	if environment == "production":
		__table_args__ = {'schema': SCHEMA}

	id = db.Column(db.Integer, primary_key=True)
	link = db.Column(db.String)
	media_url = db.Column(db.String)
	title = db.Column(db.String(100))
	description = db.Column(db.String(500))
	alt_text = db.Column(db.String(500))
	website = db.Column(db.String)
	pin_clicks = db.Column(db.Integer)
	impressions = db.Column(db.Integer)
	saves = db.Column(db.Integer)
	is_commentable = db.Column(db.Boolean(), default=True)
	notes_to_self = db.Column(db.String)
	board_id = db.Column(db.Integer, db.ForeignKey('boards.id'))
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), server_onupdate=db.func.now())

	boards = db.relationship('Board', back_populates='pins', cascade='all, delete-orphan')

	def to_dict(self):
		return {
			'id' : self.id,
			'media_url' : self.media_url,
			'title' : self.title,
			'description' : self.description,
			'alt_text' : self.alt_text,
			'website' : self.website,
			'pin_clicks' : self.pin_clicks,
			'impressions' : self.impressions,
			'saves' : self.saves,
			'is_commentable' : self.is_commentable,
			'notes_to_self' : self.notes_to_self,
			'board_id' : self.board_id
		}

	def to_dict_basic_info(self):
		return {
			'id' : self.id,
			'media_url' : self.media_url,
			'title' : self.title,
			'created_on' : self.created_on,
			'updated_on' : self.updated_on
		}
