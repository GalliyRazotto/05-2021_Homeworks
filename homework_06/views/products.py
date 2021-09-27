from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError

import logging

from models import Product
from models.database import db

log = logging.getLogger(__name__)

products_app = Blueprint("products_app", __name__)

PRODUCTS_DATA = {
    1: 'laptop',
    2: 'smartphone',
    3: 'tablet'
}


@products_app.route("/", endpoint="list")
def get_products_list():
    product = Product.query.all()
    return render_template("products/list.html", products=product)


@products_app.route("/<int:product_id>/", endpoint="detail")
def get_product(product_id: int):
    product = Product.query.filter_by(id=product_id).one_or_none()
    if product is None:
        raise NotFound(f"Not found for id {product_id}")
    return render_template("products/detail.html", product=product)


@products_app.route("/add/", methods=['GET', 'POST'], endpoint="add")
def create_product():
    if request.method == 'GET':
        return render_template("products/add.html")

    product_name = request.form.get("product-name")

    product = Product(name=product_name)
    db.session.add(product)
    try:
        db.session.commit()
    except IntegrityError:
        log.exception("Could not add product, got integrity error")
        db.session.rollback()
        raise BadRequest("Error adding new product, probably name is not unique")
    except DatabaseError:
        log.exception("Could not add product, database error")
        db.rollback()
        raise InternalServerError("Error adding new product")

    return redirect(url_for("products_app.detail", product_id=product.id))
