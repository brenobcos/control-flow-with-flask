


from flask import Blueprint, Flask

from .order_route import bp as bp_order
from .user_route import bp as bp_user

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_order)

    app.register_blueprint(bp_api)
