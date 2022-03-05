from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)

#setup mongo connection with database
app.config['MONGO_URI']="mongodb://localhost:27017/shows_db"
mongo = PyMongo(app)

#connect to collection
tv_shows = mongo.db.tv_shows

#READ
@app.route("/")
def index():
    #find all items in db and save to a variable
    all_shows = list(tv_shows.find())

    return render_template('index.html',data=all_shows)

#CREATE
@app.route("/Create", methods=["POST", "GET"])
def insert():
    if request.method=="POST":
        data = request.form 

        post_data = {'name':data['name'], 
                     'seasons': data['seasons'], 
                     'duration': data['duration'], 
                     'year':data['year'],
                     'date_added':datetime.datetime.utcnow()}

        tv_shows.insert_one(post_data)

        return "<p>Successfully Created.</p>"
    else:
        return render_template("insert.html")

#UPDATE
@app.route("/Update", methods=["POST", "GET"])
def update():
    if request.method=="POST":
        update = request.form 

        filter = {'name':update['filter']}

        to_update = {"$set": {'name':update['name'], 
                     'seasons': update['seasons'], 
                     'duration': update['duration'], 
                     'year':update['year'],
                     'date_added':datetime.datetime.utcnow()}}
        
        tv_shows.update_one(filter, to_update)

        return "<p>Successfully updated.</p>"
    else:
        return render_template("update.html")

#DELETE
@app.route("/Delete", methods=["POST", "GET"])
def delete_one():
    if request.method=="POST":
        delete = request.form 

        filter = {'name':delete['filter']}
        
        tv_shows.delete_one(filter)
        return "<p>Deleted Successfully.</p>"
    else:
        return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)
