from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from lib.environtment.address import database_URI
from lib.connector import db, ma
from lib.resources.image import ImageGCS
from lib.resources.article import Articles, Article
from lib.resources.aspiration import Aspirations, Aspiration
from lib.resources.department import Departments, Department

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)

db.init_app(app)
ma.init_app(app)

api = Api(app)

api.add_resource(ImageGCS, "/image")
api.add_resource(Articles, "/articles")
api.add_resource(Article, "/article")
api.add_resource(Aspirations, "/aspirations")
api.add_resource(Aspiration, "/aspiration")
api.add_resource(Departments, "/departments")
api.add_resource(Department, "/department")