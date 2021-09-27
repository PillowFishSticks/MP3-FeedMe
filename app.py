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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("site_recipes.html", recipes=recipes)
    


@app.route("/site_recipes")
def site_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("site_recipes.html", recipes=recipes)


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
        return redirect(url_for("get_recipes", username=session["user"]))
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
                    return redirect(url_for("get_recipes", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "created_by": request.form.get("created_by"),
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
            "notes": request.form.get("notes"),
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "time": request.form.get("time"),
            "servings": request.form.get("servings"),
            "created_by": request.form.get("created_by"),
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
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Edited")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Removed")
    return redirect(url_for("get_recipes"))


@app.route("/view_recipe")
def view_recipe():
    recipes = mongo.db.recipes.find()
    return render_template("recipe.html", recipes=recipes)

@app.route("/feedme_recipe")
def feedme_recipe():
    recipes = mongo.db.recipes.find()
    return render_template("feedme_recipe.html", recipes=recipes)

@app.route("/recipe_1")
def recipe_1():
    return render_template("recipe_1.html")


@app.route("/recipe_2")
def recipe_2():
    return render_template("recipe_2.html")


@app.route("/recipe_3")
def recipe_3():
    return render_template("recipe_3.html")


@app.route("/recipe_4")
def recipe_4():
    return render_template("recipe_4.html")


@app.route("/admin")
def admin():
    recipes = mongo.db.recipes.find()
    return render_template("admin_page.html", recipes=recipes)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
