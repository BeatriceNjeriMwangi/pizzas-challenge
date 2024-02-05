
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

metadata= MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db=SQLAlchemy(metadata=metadata)

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)

    pizzas =db.relationship("Pizza",secondary="restaurantpizza",backref="restaurant")
    restaurantspizza=db.relationship("RestaurantPizza",backref="restaurant")

class Pizza(db.Model,SerializerMixin ):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)

    restaurantspizza = db.relationship("RestaurantPizza",backref="pizza")
class RestaurantPizza(db.Model,SerializerMixin ):
    __tablename__ = 'restaurantspizzas'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)
    price=db.Column(db.Integer)