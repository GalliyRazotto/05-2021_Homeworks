from flask import Flask, request
from views.products import products_app
from models.database import db
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")


SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONN_URL", "postgresql+psycopg2://user:password@localhost:5432/postgres")

app.config.update(
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    print(request.path)
    return "<p>Hello World</p>"


@app.route("/hello/")
def hello_name():
    print(request.path)
    name = request.args.get("name", "World")
    return {
        "message": f"Hello {name}"
    }


@app.route("/item/")
@app.route("/item/<int:item>/")
def get_item(item=66):
    return {
        "message": item
    }

