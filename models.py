from config import db
from sqlalchemy_serializer import SerializerMixin

class Education_Resources(db.Model, SerializerMixin):
    __tablename__ = 'educational_resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    date_published = db.Column(db.DateTime, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Reviews(db.Model):
    __tablename__ = 'reviews'
    
    serialize_rules = ('-user',)
    
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    product_id= db.Column(db.Integer, db.ForeignKey("products.id"))
    rating = db.Column(db.String, nullable=False)
    review_text = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Events(db.Model):
    __tablename__ = 'events'
    
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    date_event = db.Column(db.DateTime, nullable=False)
    organizer = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    contact_info = db.Column(db.String, nullable=False)
    registration_deadline = db.Column(db.DateTime, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Products(db.Model):
    __tablename__ ="products"
    
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    category=db.Column(db.String, nullable=False)
    price=db.Column(db.String, nullable=False)
    eco_rating=db.Column(db.String, nullable=False)
    image_url=db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class Donations(db.Model, SerializerMixin):
    __tablename__ ="donations"
    
    serialize_rules = ('-user',)
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id",ondelete='CASCADE'))
    amount=db.Column(db.String, nullable=False)
    date=db.Column(db.DateTime, nullable=False)
    purpose=db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Partners(db.Model, SerializerMixin):
    __tablename__ ="partners"
    
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    contact_info=db.Column(db.String, nullable=False)
    website=db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class CarbonFootPrintCount(db.Model, SerializerMixin):
    __tablename__ ="carbon_footprint_counts"
    
    serialize_rules = ('-user',)
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    carbon_value=db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Impact_Monitorings(db.Model, SerializerMixin):
    __tablename__ ="impact_monitorings"
    
    serialize_rules = ('-user',)
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    
    #To be reviewed
    action_taken = db.Column(db.String, nullable=False)
    carbon_footprint = db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
class TrackGoals(db.Model, SerializerMixin):
    __tablename__ ="track_goals"
    
    serialize_rules = ('-user',)

    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    title=db.Column(db.String, nullable=False)
    description=db.Column(db.String, nullable=False)
    category=db.Column(db.String, nullable=False)
    start_date=db.Column(db.DateTime, nullable=False)
    end_date=db.Column(db.DateTime, nullable=False)
    #To be reviewed
    target_metric=db.Column(db.String, nullable=False)
    target_value=db.Column(db.String, nullable=False)
    current_value=db.Column(db.String, nullable=False)
    status=db.Column(db.String, nullable=False)
    note=db.Column(db.String, nullable=False)
    
    #To be reviewed
    reminder=db.Column(db.String, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class UserEvents(db.Model):
    __tablename__ ="user_events"
    
    serialize_rules = ('-user',)

    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'))
    event_id= db.Column(db.Integer, db.ForeignKey("events.id"))
    
    date = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    
class FeedbackForm(db.Model, SerializerMixin):
    __tablename__ ="feedback_forms"
    
    serialize_rules = ('-user',)
    
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, nullable=False) 
    feedback_message = db.Column(db.String, nullable=False) 
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    
class Users(db.Model, SerializerMixin):
    __tablename__ ="users"
    
    serialize_rules = ('-password',)
    
    id= db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String, nullable=False)
    last_name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    
    phone=db.Column(db.Integer, nullable=False)
    password=db.Column(db.String, nullable=False)
    gender=db.Column(db.String, nullable=False)
        
    role = db.Column(db.String, nullable=False)
    interests = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    reviews = db.relationship(Reviews, backref='user', cascade='all, delete-orphan')
    donations = db.relationship(Donations, backref='user', cascade='all, delete-orphan')
    carbon_footprint = db.relationship(CarbonFootPrintCount, backref='user', cascade='all, delete-orphan')
    impact_monitorings = db.relationship(Impact_Monitorings, backref='user', cascade='all, delete-orphan')
    track_goals = db.relationship(TrackGoals, backref='user', cascade='all, delete-orphan')
    events = db.relationship(UserEvents, backref='user', cascade='all, delete-orphan')