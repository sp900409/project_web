from flask  import Blueprint

item_blueprint = Blueprint('item', __name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

@item_blueprint.route('/load')
def load_item():
    """
    load an item using their store and return a JSON reprsentation of it
    :return:
    """

    pass


