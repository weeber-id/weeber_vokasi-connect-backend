from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from lib.model.event import EventModel, EventSchema
from lib.format import message, date, error
from lib.controller.crud import CRUD

Schema = EventSchema()
crud = CRUD(EventModel, Schema)

class Events(Resource):
  def get(self):
    try:
      return crud.read_all()

    except Exception as e:
      return error.CustomExceptionResponse(e)


class Event(Resource):
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


  def put(self):
    ID = request.args.get("id")
    inpt = request.get_json()

    try:
      return crud.update_by_id(ID, inpt)

    except Exception as e: 
      return error.CustomExceptionResponse(e)


  def delete(self):
    ID = request.args.get("id")

    try:
      return crud.delete_by_id(ID)
    
    except Exception as e: 
      return error.CustomExceptionResponse(e)