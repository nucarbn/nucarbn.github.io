from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_DBNAME']='restdb'
app.config['MONGO_URI']='mongodb://localhost:27017/restdb'
mongo=PyMongo(app)
@app.route('/')
def hello():
    return 'hello msg'
@app.route('/star',methods=['GET'])
def get_all_stars():
    star=mongo.db.stars
    output=[]
    for s in star.find():
        output.append({'distance':s})
        return jsonify({'result':output})
@app.route('/star/',data,methods=['POST'])
def store_data():
    star=mongo.db.stars
    distance = star.insert({'distance':data})
    output=({'distance':distance})
    return jsonify({'result':output})
if __name__=='__main__':
    app.run(debug=True)
