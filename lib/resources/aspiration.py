from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from lib.model.aspiration import AspirationModel, AspirationSchema
from lib.format import message, date, error
from lib.controller.crud import CRUD

Schema = AspirationSchema()
crud = CRUD(AspirationModel, Schema)

class Aspirations(Resource):
  @jwt_required
  def get(self):
    try:
      return crud.read_all()

    except Exception as e:
      return error.CustomExceptionResponse(e)


class Aspiration(Resource):
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