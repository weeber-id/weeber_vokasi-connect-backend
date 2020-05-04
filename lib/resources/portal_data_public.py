from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from lib.model.portal_data_public import PortalDataModel, PortalDataSchema
from lib.model.department import DepartmentModel
from lib.format import message, date, error
from lib.controller.crud import CRUD

Schema = PortalDataSchema()
crud = CRUD(PortalDataModel, Schema)

class AllPortalData(Resource):
  def get(self):
    try:
      return crud.read_all()

    except Exception as e:
      return error.CustomExceptionResponse(e)


class PortalData(Resource):
  def get(self):
    ID = request.args.get("id")

    try:
      return crud.read_by_id(ID)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def post(self):
    inpt = request.get_json()

    try:
      ID = inpt["department_id"]
      department = DepartmentModel.find_by_id(ID)
      if department is None:
        return {"message": message.DATA_NOT_FOUND}, 404
      
      inpt["department"] = department
      modeldata = PortalDataModel(**inpt)
      return CRUD.create_from_model(modeldata)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def put(self):
    ID = request.args.get("id")
    inpt = request.get_json()

    try:
      department = DepartmentModel.find_by_id(inpt["department_id"])
      datamodel = PortalDataModel.find_by_id(ID)
      if (department is None) or (datamodel is None):
        return {"message": message.DATA_NOT_FOUND}, 404

      inpt["department"] = department
      return crud.update_from_model(datamodel, inpt)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def delete(self):
    ID = request.args.get("id")

    try:
      return crud.delete_by_id(ID)
    
    except Exception as e: 
      return error.CustomExceptionResponse(e)