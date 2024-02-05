
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates

metadata= MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db=SQLAlchemy(metadata=metadata)

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    address=db.Column(db.String)

    pizza =db.relationship("Pizza",secondary="restaurant_pizzas",backref="restaurant",viewonly=True)
    restaurant_pizza=db.relationship("RestaurantPizza",backref="restaurant")

class Pizza(db.Model,SerializerMixin ):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)

    restaurant_pizza = db.relationship("RestaurantPizza",backref="pizza")
class RestaurantPizza(db.Model,SerializerMixin ):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    restaurants_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizzas_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow,onupdate=datetime.utcnow)
    price=db.Column(db.Integer)

@validates('price')
def validates_price(self,key,price):
    if not 1 <= price <= 30:
        raise ValueError("price must be between 1 and 30")
    return price