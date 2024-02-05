from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from datetime import datetime
from models import db,Restaurant,Pizza,RestaurantPizza
from app import app

fake=Faker()
app.app_context().push()


def seed_data():
    db.session.query(Restaurant).delete()
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.commit()

    #restaurants creating
    rest1=Restaurant(name='Cafe',address='Thika')
    rest2=Restaurant(name='demo',address='Tunnel')
    rest3=Restaurant(name='moringa',address='Ngong')
    rest4=Restaurant(name='naz',address='Ronga')
    rest5=Restaurant(name='sonford',address='cbd')


    First_pizza=Pizza(name='First',ingredients='peperoni')
    Second_pizza=Pizza(name='Second',ingredients='tikka')
    Third_pizza=Pizza(name='third',ingredients='bbq')
    Fourth_pizza=Pizza(name='fourth',ingredients='periperi')
    Fifth_pizza=Pizza(name='fifth',ingredients='tikka')


    db.session.add_all([rest1,rest2,rest3,rest4,rest5,First_pizza,Second_pizza,Third_pizza,Fourth_pizza,Fifth_pizza])
    db.session.commit()

if __name__ == '__main__':
    seed_data()
