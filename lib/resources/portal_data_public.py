from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from lib.model.portal_data_public import PortalDataModel, PortalDataSchema
from lib.model.category import CategoryModel, CategorySchema
from lib.format import message, date, error
from lib.controller.crud import CRUD

portaldata_schema = PortalDataSchema()
category_schema = CategorySchema()

crud_portaldata = CRUD(PortalDataModel, portaldata_schema)
crud_category = CRUD(CategoryModel, category_schema)

class AllPortalData(Resource):
  def get(self):
    try:
      return crud_portaldata.read_all()

    except Exception as e:
      return error.CustomExceptionResponse(e)


class PortalData(Resource):
  def get(self):
    ID = request.args.get("id")

    try:
      return crud_portaldata.read_by_id(ID)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def post(self):
    inpt = request.get_json()

    try:
      category_id = inpt["category_id"]
      category = crud_category.find_by_id(category_id, exception=True)
      inpt["category"] = category
      
      modeldata = PortalDataModel(**inpt)
      return CRUD.create_from_model(modeldata)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def put(self):
    ID = request.args.get("id")
    inpt = request.get_json()

    try:
      datamodel = crud_portaldata.find_by_id(ID, exception=True)

      category_id = inpt["category_id"]
      category = crud_category.find_by_id(category_id, exception=True)
      inpt["category"] = category

      return crud_portaldata.update_from_model(datamodel, inpt)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def delete(self):
    ID = request.args.get("id")

    try:
      return crud_portaldata.delete_by_id(ID)
    
    except Exception as e: 
      return error.CustomExceptionResponse(e)