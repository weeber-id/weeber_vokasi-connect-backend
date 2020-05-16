from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from lib.environtment.address import database_URI
from lib.connector import db, ma
from lib.resources.image import ImageGCS
from lib.resources.article import Articles, Article
from lib.resources.aspiration import Aspirations, Aspiration
from lib.resources.category import Categories
from lib.resources.department import Departments, Department
from lib.resources.event import Events, Event
from lib.resources.portal_data_public import AllPortalData, PortalData
from lib.resources.ruang_prestasi import AllRuangPrestasi, RuangPrestasi

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
api.add_resource(Categories, "/categories")
api.add_resource(Departments, "/departments")
api.add_resource(Department, "/department")
api.add_resource(Events, "/events")
api.add_resource(Event, "/event")
api.add_resource(AllPortalData, "/all-portal-data")
api.add_resource(PortalData, "/portal-data")
api.add_resource(AllRuangPrestasi, "/all-ruang-prestasi")
api.add_resource(RuangPrestasi, "/ruang-prestasi")