import json

from flask import Flask
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from app import Constants
from app.models_configuration import configure as config_db, db
from app.serealizer import configure as config_ma
from app.controllers.Reseller_Controller import reseller_bp
from app.controllers.Purchase_Controller import purchase_bp
from app.controllers.Purchase_Status_Controller import purchase_status_bp
from app.controllers.Cashback_Controller import cashback_bp


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Constants.DB_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

config_db(app)
config_ma(app)

Migrate(app, app.db)

app.register_blueprint(purchase_bp)
app.register_blueprint(cashback_bp)
app.register_blueprint(purchase_status_bp)
app.register_blueprint(reseller_bp)


@app.errorhandler(HTTPException)
def handle_exception(e):

    response = e.get_response()

    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = Constants.JSON_CONTENT

    return response

