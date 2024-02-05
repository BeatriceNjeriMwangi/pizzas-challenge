from flask import Flask,jsonify,request,make_response
from flask_migrate import Migrate
from flask_restful import Api,Resource

from models import db, Restaurant, RestaurantPizza,Pizza

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
migrate=Migrate(app,db)
db.init_app(app)
api=Api(app)

class Restaurants(Resource):
    def get(self):
        response_dict=[{"id":restaurant.id,"name":restaurant.name,"address":restaurant.address}for restaurant in Restaurant.query.all()]
        return make_response(jsonify(response_dict),200)
    
class RestaurantById(Resource):
    def get(self, id):
        restaurant=Restaurant.query.filter_by(id=id).first().to_dict()
        if not restaurant:
            return make_response(jsonify({"error":"Restaurant not found"}))
        restaurant_data={
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address,
            "pizzas":[]
            
        }
        for pizza in restaurant.pizzas:
            response={
                "id":pizza.id,
                "name":pizza.name,
                "ingredients":pizza.ingredients
            }
        restaurant_data["pizzas"].append(response) 

        return make_response(jsonify(restaurant),200) 

    def delete(Resource):
        restaurant=Restaurant.query.filter_by(id=id).first().to_dict()

        if not restaurant:
            return make_response(jsonify({
  "error": "Restaurant not found"
}))
        RestaurantPizza.query.filter_by(id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return make_response(jsonify({}),200)
    
class Pizza(Resource):
    def get(self):
        pizza=[{"id":pizza.id,"name":pizza.name,"ingredients":pizza.ingredients}for pizza in Pizza.query.all()]
        return make_response(jsonify(pizza),200)
    
api.add_resource(Restaurants,'/restaurants')
api.add_resource(RestaurantById,'/restaurants/<int:id>')
api.add_resource(Pizza,'/pizzas')





if __name__ == "__main__":
    app.run(PORT=5555)