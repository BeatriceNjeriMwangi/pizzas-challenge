from flask import Flask,jsonify,request,make_response
from flask_migrate import Migrate
from flask_restful import Api,Resource

from models import db,Restaurant,RestaurantPizza,Pizza,Rest

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
migrate=Migrate(app.db)
db.init_app(app)
api=Api(app)









if __name__ == "__main__":
    app.run(PORT=5555)