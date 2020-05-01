from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from lib.model.department import DepartmentModel, DepartmentSchema
from lib.format import message, date, error
from lib.controller.crud import CRUD

Schema = DepartmentSchema()
crud = CRUD(DepartmentModel, Schema)

class Departments(Resource):
  def get(self):
    try:
      return crud.read_all()

    except Exception as e:
      return error.CustomExceptionResponse(e)


class Department(Resource):
  def get(self):
    ID = request.args.get("id")

    try:
      return crud.read_by_id(ID)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def post(self):
    inpt = request.get_json()

    try:
      return crud.create(inpt)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def delete(self):
    ID = request.args.get("id")

    try:
      return crud.delete_by_id(ID)
    
    except Exception as e: 
      return error.CustomExceptionResponse(e)