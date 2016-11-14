from flask import Blueprint
from flask import json
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from src.models.stores.store import Store

store_blueprint = Blueprint('stores', __name__)


@store_blueprint.route('/')
def index():
    stores = Store.all()
    return render_template("stores/store_index.jinja2", stores = stores)


@store_blueprint.route('/store/<string:store_id>')
def store_page(store_id):
    return render_template("stores/store.jinja2", store=Store.get_by_id(store_id))


@store_blueprint.route('/create', methods=['GET', 'POST'])
def create_store():
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Store(name, url_prefix, tag_name, query).save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('stores/create_store.jinja2')

@store_blueprint.route('/edit/<string:store_id>', methods=['GET', 'POST'])
def edit_store(store_id):
    if request.method == 'POST':
        pass
    return "Edit store page"

@store_blueprint.route('/delete/<string:store_id>')
def delete_store(store_id):
    return "Delete store"
