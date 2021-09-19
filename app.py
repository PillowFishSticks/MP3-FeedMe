import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    if "user" in session:
        user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        return render_template("index.html", user=user)
    else:
        return render_template("index.html")


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("your_recipes.html", recipes=recipes)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Success")
        return redirect(url_for("your_recipes", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("your_recipes", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


@app.route("/your_recipes/<username>", methods=["GET", "POST"])
def your_recipes(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session ["user"]:
        return render_template("your_recipes.html", username=username)
    
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {

            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "ingredient_8": request.form.get("ingredient_8"),
            "ingredient_9": request.form.get("ingredient_9"),
            "direction_1": request.form.get("direction_1"),
            "direction_2": request.form.get("direction_2"),
            "direction_3": request.form.get("direction_3"),
            "direction_4": request.form.get("direction_4"),
            "direction_5": request.form.get("direction_5"),
            "direction_6": request.form.get("direction_6"),
            "direction_7": request.form.get("direction_7"),
            "direction_8": request.form.get("direction_8"),
            "direction_9": request.form.get("direction_9"),
            "notes": request.form.get("notes")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


@app.route("/view_recipe")
def view_recipe():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipe.html", recipes=recipes)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
