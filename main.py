from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from lib.environtment.address import MYSQL_ADDRESS
from lib.connector import db, ma
from lib.resources.link_tree import Link_tree

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://vokasiapi:mastervokasiconnectapi@{}/vokasi_connect".format(MYSQL_ADDRESS)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)

db.init_app(app)
ma.init_app(app)

api = Api(app)

api.add_resource(Link_tree, "/link_tree")